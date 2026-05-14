import random
import json
import allure
from allure_commons.types import AttachmentType
from faker import Faker

from logger.logger import Logger
from services.univesity.models.base_student import DegreeEnum
from services.univesity.models.group_request import GroupRequest
from services.univesity.models.student_request import StudentRequest
from services.univesity.university_service import UniversityService

faker = Faker()

@allure.epic("University Management")
@allure.feature("Student Portal")
class TestStudent:
    @allure.title("Успешное создание студента внутри группы")
    @allure.story("Создание учетных записей студентов")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.id("STUDENT-01")
    def test_student_create(self, university_api_utils_admin):

        university_service = UniversityService(api_utils=university_api_utils_admin)
        with allure.step("Шаг 1. Создание учебной группы"):
            group_name = faker.name()
            group = GroupRequest(name=faker.name())
            allure.attach(
                json.dumps({"name": group_name}, index=4),
                name="Request Group JSON",
                attachment_type=AttachmentType.JSON
            )
            group_response = university_service.create_group(group_request=group)
            Logger.info(f"### Step 1 Complete. Group Created ID: {group_response.id}")

        Logger.info("### Step 2. Create student")
        with allure.step("Шаг 2. Создание студента"):
            student = StudentRequest(first_name=faker.first_name(),
                                     last_name=faker.last_name(),
                                     email=faker.email(),  # noqa Expected type 'EmailStr', got 'str' instead
                                     degree=random.choice([option for option in DegreeEnum]),
                                     phone=faker.numerify("+7##########"),
                                     group_id=group_response.id)
            student_response = university_service.create_student(student_request=student)
        with allure.step("Шаг 3. Валидация ID группы в ответе сервера"):
            allure.attach(
                f"Expected Group ID: {group_response.id}\nActual Group ID: {student_response.group_id}",
                name="Comparison Metadata",
                attachment_type=AttachmentType.TEXT
            )

            assert student_response.group_id == group_response.id, \
                f"Wrong group id. Actual: '{group_response.id}', but expected: '{student_response.group_id}'"
