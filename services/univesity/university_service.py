import os
from dotenv import load_dotenv
from services.general.base_service import BaseService
from services.general.models.success_response import SuccessResponse
from services.univesity.helpers.grade_helper import GradeHelper
from services.univesity.helpers.grade_stats_helper import GradeStatsHelper
from services.univesity.helpers.group_helper import GroupHelper
from services.univesity.helpers.student_helper import StudentHelper
from services.univesity.helpers.teacher_helper import TeacherHelper
from services.univesity.models.grade_request import GradeRequest
from services.univesity.models.grade_response import GradeResponse
from services.univesity.models.grade_stats_response import GradeStatsResponse
from services.univesity.models.group_request import GroupRequest
from services.univesity.models.group_response import GroupResponse
from services.univesity.models.student_request import StudentRequest
from services.univesity.models.student_response import StudentResponse
from services.univesity.models.teacher_request import TeacherRequest
from services.univesity.models.teacher_response import TeacherResponse
from utils.api_utils import ApiUtils

load_dotenv()


class UniversityService(BaseService):
    SERVICE_URL = os.getenv("UNIVERSITY_SERVICE_API_URL")

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)
        self.grade_helper = GradeHelper(self.api_utils)
        self.grade_stats_helper = GradeStatsHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def create_teacher(self, teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def create_grade(self, grade_request: GradeRequest) -> GradeResponse:
        response = self.grade_helper.post_grade(data=grade_request.model_dump())
        return GradeResponse(**response.json())

    def delete_group(self, group_id: int | str) -> SuccessResponse:
        response = self.group_helper.delete_group(group_id)
        return SuccessResponse(**response.json())

    def delete_student(self, student_id: int | str) -> SuccessResponse:
        response = self.student_helper.delete_student(student_id)
        return SuccessResponse(**response.json())

    def delete_teacher(self, teacher_id: int | str) -> SuccessResponse:
        response = self.teacher_helper.delete_teacher(teacher_id)
        return SuccessResponse(**response.json())

    def delete_grade(self, grade_id: int | str) -> SuccessResponse:
        response = self.grade_helper.delete_grade(grade_id)
        return SuccessResponse(**response.json())

    def get_grade_stats(
            self,
            student_id: int | None = None,
            teacher_id: int | None = None,
            group_id: int | None = None
    ) -> GradeStatsResponse:
        response = self.grade_stats_helper.get_grades_stats(
            student_id=student_id,
            teacher_id=teacher_id,
            group_id=group_id
        )
        return GradeStatsResponse(**response.json())
