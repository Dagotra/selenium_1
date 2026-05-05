from faker import Faker
from .utils.soft_assert import SoftAssert
from .conftest import ThreeGradeData
from services.univesity.models.grade_response import GradeResponse
from services.univesity.university_service import UniversityService

faker = Faker()


class TestGradeStatsGet:
    def test_count_grade_stats_teacher(self, university_api_utils_admin, create_three_grades: ThreeGradeData):
        """Проверка наличия 2 оценок в статистике оценок, через фильтр 'teacher_id'"""

        soft_assert = SoftAssert()
        university_service = UniversityService(api_utils=university_api_utils_admin)
        teacher_id = create_three_grades.teacher_id_2
        stats = university_service.get_grade_stats(teacher_id=teacher_id)
        grade_1 = create_three_grades.grade_2.grade
        grade_2 = create_three_grades.grade_3.grade
        list_grade = [grade_1, grade_2]

        expected_grades_count = len(list_grade)
        expected_min_grade = min(list_grade)
        expected_max_grade = max(list_grade)
        expected_avg = (grade_1 + grade_2) / expected_grades_count

        soft_assert.assert_equal(stats.count, expected_grades_count, msg="Wrong grade count: filter 'teacher_id'")
        soft_assert.assert_equal(stats.min, expected_min_grade, msg="Wrong value min grade: filter 'teacher_id'")
        soft_assert.assert_equal(stats.max, expected_max_grade, msg="Wrong value max grade: filter 'teacher_id'")
        soft_assert.assert_equal(stats.avg, expected_avg, msg="Wrong value avg grade : filter 'teacher_id'")
        soft_assert.check()

    def test_count_grade_stats_group(self, university_api_utils_admin, create_three_grades: ThreeGradeData):
        """Проверка наличия 3 оценок в статистике оценок, через фильтр 'group_id'"""
        expected_grades_count = 3
        soft_assert = SoftAssert()
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group_id = create_three_grades.group_id
        stats = university_service.get_grade_stats(group_id=group_id)

        grade_1 = create_three_grades.grade_1.grade
        grade_2 = create_three_grades.grade_2.grade
        grade_3 = create_three_grades.grade_3.grade

        list_grade = [grade_1, grade_2, grade_3]
        count_grade = len(list_grade)
        expected_min_grade = min(list_grade)
        expected_max_grade = max(list_grade)
        expected_avg = (grade_1 + grade_2 + grade_3) / count_grade

        soft_assert.assert_equal(stats.count, expected_grades_count, msg="Wrong grade count filter 'group_id'")
        soft_assert.assert_equal(stats.min, expected_min_grade, msg="Wrong value min grade: filter 'group_id'")
        soft_assert.assert_equal(stats.max, expected_max_grade, msg="Wrong value max grade: filter 'group_id'")
        soft_assert.assert_equal(stats.avg, expected_avg, msg="Wrong value avg grade : filter 'group_id'")
        soft_assert.check()

    def test_avg_grades_stats_student(self,
                                      university_api_utils_admin,
                                      create_three_grades: ThreeGradeData
                                      ):
        """
        Проверка количества оценок используя фильтр 'student_id'.
        Проверка min и max оценок используя фильтр 'student_id'.
        Проверка валидного avg оценок, используя фильтр 'student_id', у которого есть три оценки.
        """
        university_service = UniversityService(api_utils=university_api_utils_admin)
        soft_assert = SoftAssert()

        stats_response = university_service.get_grade_stats(student_id=create_three_grades.student_id)

        grade_1 = create_three_grades.grade_1.grade
        grade_2 = create_three_grades.grade_2.grade
        grade_3 = create_three_grades.grade_3.grade

        list_grade = [grade_1, grade_2, grade_3]
        count_grade = len(list_grade)
        expected_min_grade = min(list_grade)
        expected_max_grade = max(list_grade)
        expected_avg = (grade_1 + grade_2 + grade_3) / count_grade

        soft_assert.assert_equal(stats_response.count, count_grade, msg="Wrong grade count filter 'student_id'")
        soft_assert.assert_equal(stats_response.min, expected_min_grade, msg="Wrong min grade filter 'student_id'")
        soft_assert.assert_equal(stats_response.max, expected_max_grade, msg="Wrong max grade filter 'student_id'")
        soft_assert.assert_equal(stats_response.avg, expected_avg, msg="Wrong actual value avg grades")
        soft_assert.check()

    def test_general_grade_stats(self, university_api_utils_admin, create_and_delete_grade: GradeResponse):
        """Проверка общей статистки оценок без фильтров, где проверяется count >= 1; min, max, avg - не None"""
        university_service = UniversityService(api_utils=university_api_utils_admin)
        stats_response = university_service.get_grade_stats()
        soft_assert = SoftAssert()

        soft_assert.assert_true(stats_response.count >= 1, msg="General count grades should be >= 1")
        soft_assert.assert_not_none(stats_response.min, msg="min is None")
        soft_assert.assert_not_none(stats_response.max, msg="max is None")
        soft_assert.assert_not_none(stats_response.avg, msg="avg is None")
        soft_assert.check()

    def test_grade_count_none_teacher(self, university_api_utils_admin, create_and_delete_grade: GradeResponse):
        """Проверка, get stats через фильтр 'teacher_id' - не существует"""
        university_service = UniversityService(api_utils=university_api_utils_admin)

        # На бэке в фильтре можно выставить отрицательный ID
        stat_response = university_service.get_grade_stats(teacher_id=-1)
        soft_assert = SoftAssert()
        expected_count = 0

        expected_value_grade = None

        soft_assert.assert_equal(stat_response.count, expected_count, msg="Wrong count grade, should be 0")
        soft_assert.assert_equal(stat_response.min, expected_value_grade, msg="Wrong min value grade, should be None")
        soft_assert.assert_equal(stat_response.max, expected_value_grade, msg="Wrong max value grade, should be None")
        soft_assert.assert_equal(stat_response.avg, expected_value_grade, msg="Wrong avg value grade, should be None")
        soft_assert.check()
