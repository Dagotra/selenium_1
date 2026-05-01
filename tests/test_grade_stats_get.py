from faker import Faker

from services.univesity.models.base_grade import MIN_GRADE, MAX_GRADE
from .conftest import TwoGradeData
from services.univesity.models.grade_response import GradeResponse
from services.univesity.university_service import UniversityService

faker = Faker()


class TestGradeStatsGet:
    def test_grade_stats_teacher(self, university_api_utils_admin, create_two_grades: TwoGradeData, soft_assert):
        expected_grades_count = 1

        university_service = UniversityService(api_utils=university_api_utils_admin)
        teacher_id = create_two_grades.teacher_id_1
        stats = university_service.get_grade_stats(teacher_id=teacher_id)

        soft_assert.assert_equal(stats.count, expected_grades_count, msg="Wrong grade count")
        soft_assert.assert_not_none(stats.min, msg="min is None")
        soft_assert.assert_not_none(stats.max, msg="max is None")
        soft_assert.assert_not_none(stats.avg, msg="avg is None")
        soft_assert.assert_range(stats.min, MIN_GRADE, MAX_GRADE, msg="Min grade out of range")
        soft_assert.assert_range(stats.max, MIN_GRADE, MAX_GRADE, msg="Max grade out of range")

    def test_grade_stats_student(self,
                                 university_api_utils_admin,
                                 create_two_grades: TwoGradeData,
                                 soft_assert):
        university_service = UniversityService(api_utils=university_api_utils_admin)

        stats_response = university_service.get_grade_stats(student_id=create_two_grades.student_id)
        count_grade = 2
        grade_1 = create_two_grades.grade_1.grade
        grade_2 = create_two_grades.grade_2.grade
        expected_avg = (grade_1 + grade_2) / count_grade
        soft_assert.assert_not_none(stats_response.min, msg="min is None")
        soft_assert.assert_not_none(stats_response.max, msg="max is None")
        soft_assert.assert_not_none(stats_response.avg, msg="avg is None")
        soft_assert.assert_equal(stats_response.avg, expected_avg, msg="Wrong actual value avg grades")

    def test_general_grade_stats(self, university_api_utils_admin, create_and_delete_grade: GradeResponse, soft_assert):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        stats_response = university_service.get_grade_stats()
        soft_assert.assert_not_none(stats_response.min, msg="min is None")
        soft_assert.assert_not_none(stats_response.max, msg="max is None")
        soft_assert.assert_not_none(stats_response.avg, msg="avg is None")
