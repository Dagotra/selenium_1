from faker import Faker

from services.univesity.models.two_grade_data import TwoGradeData
from services.univesity.models.grade_response import GradeResponse
from services.univesity.models.grade_stats_request import GradeStatsRequest
from services.univesity.university_service import UniversityService

faker = Faker()


class TestGradeStatsGet:
    def test_grade_stats_teacher(self, university_api_utils_admin, create_two_grades: TwoGradeData):
        expected_grades_count = 1

        university_service = UniversityService(api_utils=university_api_utils_admin)
        teacher_1_id, teacher_2_id = create_two_grades.teacher_id_1, create_two_grades.teacher_id_2
        stats = GradeStatsRequest(teacher_id=teacher_1_id)
        stats_response = university_service.get_grade_stats(grade_stats=stats)

        assert stats_response.count == expected_grades_count, \
            (f"For teacher with id: '{teacher_1_id}', expected grades count: '{expected_grades_count}, "
             f"but actual count: '{stats_response.count}'")
        assert stats_response.max is not None, f"The query filter returns '{stats_response.max}' values"
        assert stats_response.min is not None, f"The query filter returns '{stats_response.min}' values"
        assert stats_response.avg is not None, f"The query filter returns '{stats_response.avg}' values"

    def test_grade_stats_student(self, university_api_utils_admin, create_and_delete_grade: GradeResponse):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        student = create_and_delete_grade.student_id

        stats = GradeStatsRequest(student_id=student)
        stats_response = university_service.get_grade_stats(grade_stats=stats)
        assert stats_response.max is not None, f"The query filter returns '{stats_response.max}' values"
        assert stats_response.min is not None, f"The query filter returns '{stats_response.min}' values"
        assert stats_response.avg is not None, f"The query filter returns '{stats_response.avg}' values"

    def test_general_grade_stats(self, university_api_utils_admin, create_and_delete_grade: GradeResponse):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        general_stats = GradeStatsRequest()
        stats_response = university_service.get_grade_stats(general_stats)
        assert stats_response.max is not None, f"The query filter returns '{stats_response.max}' values"
        assert stats_response.min is not None, f"The query filter returns '{stats_response.min}' values"
        assert stats_response.avg is not None, f"The query filter returns '{stats_response.avg}' values"
