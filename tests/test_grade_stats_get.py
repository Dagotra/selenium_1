from services.univesity.models.grade_response import GradeResponse
from services.univesity.models.grade_stats_request import GradeStatsRequest
from services.univesity.university_service import UniversityService


class TestGradeStatsGet:
    def test_grade_stats_teacher(self, university_api_utils_admin, create_and_delete_grade: GradeResponse):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        teacher = create_and_delete_grade.teacher_id

        stats = GradeStatsRequest(student_id=teacher)
        stats_response = university_service.get_grade_stats(grade_stats=stats)
        print(stats_response.count)

    def test_grade_stats_student(self, university_api_utils_admin, create_and_delete_grade: GradeResponse):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        student = create_and_delete_grade.student_id

        stats = GradeStatsRequest(student_id=student)
        stats_response = university_service.get_grade_stats(grade_stats=stats)
        print(stats_response.count)

    def test_general_grade_stats(self, university_api_utils_admin, create_and_delete_grade: GradeResponse):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        general_stats = GradeStatsRequest()
        stats_response = university_service.get_grade_stats(general_stats)