import pytest
import random
from logger.logger import Logger
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.univesity.models.base_student import DegreeEnum
from services.univesity.models.base_teacher import SubjectEnum
from services.univesity.models.grade_request import GradeRequest
from services.univesity.models.group_request import GroupRequest
from services.univesity.models.student_request import StudentRequest
from services.univesity.models.teacher_request import TeacherRequest
from services.univesity.university_service import UniversityService
from utils.api_utils import ApiUtils
from faker import Faker

from tests.utils.soft_assert import SoftAssert

faker = Faker()

from services.univesity.models.grade_response import GradeResponse
from dataclasses import dataclass


@dataclass
class TwoGradeData:
    teacher_id_1: int
    teacher_id_2: int
    student_id: int
    grade_1: GradeResponse
    grade_2: GradeResponse


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def auth_service_anonym(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    return auth_service


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_service_anonym):
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)

    auth_service_anonym.register_user(
        register_request=RegisterRequest(username=username,
                                         password=password,
                                         password_repeat=password,
                                         email=faker.email()))  # noqa Expected type 'EmailStr', got 'str' instead

    login_response = auth_service_anonym.login_user(login_requests=LoginRequest(username=username, password=password))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def create_and_delete_group(university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)

    group = GroupRequest(name=faker.name())
    group_response = university_service.create_group(group_request=group)
    group_id = group_response.id
    group_name = group_response.name
    Logger.info(f"### Step-group 1. Create group with id: '{group_id}' , name: '{group_name}'")
    yield group_response
    university_service.delete_group(group_id)
    Logger.info(f"### Step-group 2. Delete group with id: '{group_id}' , name: '{group_name}'")


@pytest.fixture(scope="function", autouse=False)
def create_and_delete_student(university_api_utils_admin, create_and_delete_group):
    """Студент может создаваться только при создании группы, используется фикстура создания и удаления группы"""
    university_service = UniversityService(api_utils=university_api_utils_admin)
    group_id = create_and_delete_group.id
    student = StudentRequest(first_name=faker.first_name(),
                             last_name=faker.last_name(),
                             email=faker.email(),  # noqa Expected type 'EmailStr', got 'str' instead
                             degree=random.choice([option for option in DegreeEnum]),
                             phone=faker.numerify("+7##########"),
                             group_id=group_id)
    student_response = university_service.create_student(student_request=student)
    student_id = student_response.id
    student_first_name = student_response.first_name

    Logger.info(f"### Step-student 1. Create student with id: '{student_id}' , name: '{student_first_name}'")
    yield student_response
    university_service.delete_student(student_id)
    Logger.info(f"### Step-student 2. Delete student with id: '{student_id}' , name: '{student_first_name}'")


@pytest.fixture(scope="function", autouse=False)
def create_and_delete_teacher(university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    teacher = TeacherRequest(first_name=faker.first_name(),
                             last_name=faker.last_name(),
                             subject=random.choice([subject for subject in SubjectEnum]))
    teacher_response = university_service.create_teacher(teacher_request=teacher)
    teacher_id = teacher_response.id
    teacher_last_name = teacher_response.last_name
    Logger.info(f"### Step-teacher 1. Create teacher with id: '{teacher_id}', last name: '{teacher_last_name}'")
    yield teacher_response
    status = university_service.delete_teacher(teacher_response.id)
    Logger.info(f"{status}")
    Logger.info(f"### Step-teacher 2. Delete teacher with id: '{teacher_id}', last name: '{teacher_last_name}'")


@pytest.fixture(scope="function", autouse=False)
def create_and_delete_grade(university_api_utils_admin, create_and_delete_teacher, create_and_delete_student):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    grade = GradeRequest(teacher_id=create_and_delete_teacher.id,
                         student_id=create_and_delete_student.id,
                         grade=random.randint(0, 5))
    grade_response = university_service.create_grade(grade_request=grade)
    grade_id = grade_response.id

    Logger.info(f"### Step-grade 1. Create grade with id: '{grade_id}'")
    yield grade_response
    university_service.delete_grade(grade_id)
    Logger.info(f"### Step-grade 2. Delete grade with id: '{grade_id}'")


@pytest.fixture(scope="function", autouse=False)
def create_two_grades(university_api_utils_admin, create_and_delete_student):
    """Создает оценки у двух разных учителей и студентов """
    university_service = UniversityService(api_utils=university_api_utils_admin)
    teacher_1 = TeacherRequest(first_name="one" + faker.first_name(),
                               last_name="one" + faker.last_name(),
                               subject=random.choice([subject for subject in SubjectEnum]))
    teacher_id_1 = university_service.create_teacher(teacher_request=teacher_1).id
    Logger.info(f"### Step-teacher 1.1: Create one teacher with id: {teacher_id_1}")

    student_id_1 = create_and_delete_student.id
    Logger.info(f"### Step-student 1.2: Create one student with id: {student_id_1}")
    teacher_2 = TeacherRequest(first_name="two" + faker.first_name(),
                               last_name="two" + faker.last_name(),
                               subject=random.choice([subject for subject in SubjectEnum]))
    one_grade = GradeRequest(teacher_id=teacher_id_1,
                             student_id=student_id_1,
                             grade=random.randint(0, 5))

    grade_1 = university_service.create_grade(grade_request=one_grade)
    Logger.info(f"### Step-grade 1.3: Create one grade with id: {grade_1.id}")

    teacher_id_2 = university_service.create_teacher(teacher_request=teacher_2).id
    Logger.info(f"### Step-teacher 1.4: Create two teacher with id: {teacher_id_2}")
    two_grade = GradeRequest(teacher_id=teacher_id_2,
                             student_id=student_id_1,
                             grade=random.randint(0, 5))

    grade_2 = university_service.create_grade(grade_request=two_grade)

    Logger.info(f"### Step-grade 1.5: Create two grade with id: {grade_2.id}")

    yield TwoGradeData(
        teacher_id_1=teacher_id_1,
        teacher_id_2=teacher_id_2,
        student_id=student_id_1,
        grade_1=grade_1,
        grade_2=grade_2,
    )

    Logger.info(f"### Step-grade 2.1 Delete one grade with id: '{grade_1.id}'")
    university_service.delete_grade(grade_1.id)

    Logger.info(f"### Step-grade 2.2. Delete two grade with id: '{grade_2.id}'")
    university_service.delete_grade(grade_2.id)

    Logger.info(f"### Step-teacher 2.3: Delete one teacher with id: {teacher_id_1}")
    university_service.delete_teacher(teacher_id_1)

    Logger.info(f"### Step-teacher 2.4: Delete two teacher with id: {teacher_id_2}")
    university_service.delete_teacher(teacher_id_2)


@pytest.fixture(scope="function", autouse=False)
def soft_assert():
    sa = SoftAssert()
    yield sa
    sa.check()
