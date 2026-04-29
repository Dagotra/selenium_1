import random

from faker import Faker

from logger.logger import Logger
from services.univesity.models.base_student import DegreeEnum
from services.univesity.models.group_request import GroupRequest
from services.univesity.models.student_request import StudentRequest
from services.univesity.university_service import UniversityService

faker = Faker()


class TestStudent:
    def test_student_create(self, university_api_utils_admin):
        Logger.info("### Step 1. Create group")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)

        Logger.info("### Шаг 2. Create student")
        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),  # noqa Expected type 'EmailStr', got 'str' instead
                                 degree=random.choice([option for option in DegreeEnum]),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group_response.id)
        student_response = university_service.create_student(student_request=student)

        assert student_response.group_id == group_response.id, \
            (f"Wrong group id. "
             f"Actual: '{group_response.id}', but excepted: '{student_response.id}'")
