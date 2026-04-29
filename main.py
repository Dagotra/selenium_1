import random
from faker import Faker

from services.auth.helpers.authorization_helper import AuthorizationHelper
from services.univesity.helpers.group_helper import GroupHelper
from services.univesity.helpers.student_helper import StudentHelper
from services.auth.helpers.user_helper import UserHelper
from utils.api_utils import ApiUtils

AUTH_URL = 'http://localhost:8000'
UNIVERSITY_URL = 'http://localhost:8001'
REGISTER_ENDPOINT = '/auth/register/'
LOGIN_ENDPOINT = '/auth/login/'
USERS_ME_ENDPOINT = '/users/me/'
GROUPS_ENDPOINT = '/groups/'
STUDENTS_ENDPOINT = '/students/'

faker = Faker()
user_name = faker.user_name()
password = "aZ!$" + faker.word() + '123<>'
user_email = faker.email()
# anonym_auth_api_utils = ApiUtils(AUTH_URL) Можно выставить в аргумент класса AuthorizationHelper
authorization_helper = AuthorizationHelper(api_utils=ApiUtils(AUTH_URL))
response = authorization_helper.post_register(
    data={
        "username": user_name,
        "password": password,
        "password_repeat": password,
        "email": user_email
    }
)
response = authorization_helper.post_login(
    data={
        "username": user_name,
        "password": password
    }
)
access_token = response.json()["access_token"]

admin_auth_api_utils = ApiUtils(AUTH_URL, headers={"Authorization": f"Bearer {access_token}"})
user_admin_helper = UserHelper(admin_auth_api_utils)

admin_university_api_utils = ApiUtils(UNIVERSITY_URL, headers={"Authorization": f"Bearer {access_token}"})
group_admin_helper = GroupHelper(admin_university_api_utils)
student_admin_helper = StudentHelper(admin_university_api_utils)

response = user_admin_helper.get_me()
response = group_admin_helper.post_group(json={"name": faker.word()})
response = student_admin_helper.post_student(
    json={
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": user_email,
        "degree": random.choice(["Associate",
                                 "Bachelor",
                                 "Master",
                                 "Doctorate"]),
        "phone": faker.numerify("+7##########"),
        "group_id": response.json()["id"]
    },
)
