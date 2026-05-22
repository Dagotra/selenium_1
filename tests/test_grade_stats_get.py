import pytest
from faker import Faker
from .utils.soft_assert import SoftAssert
from .conftest import ThreeGradeData
from services.univesity.models.grade_response import GradeResponse
from services.univesity.university_service import UniversityService

faker = Faker()
NONEXISTENT_ID = 9999999999


class TestGradeStatsGet:
    def test_get_teacher_stats(self, university_api_utils_admin, create_three_grades: ThreeGradeData):
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

    def test_get_group_stats(self, university_api_utils_admin, create_three_grades: ThreeGradeData):
        """Проверка наличия 3 оценок в статистике оценок, через фильтр 'group_id'"""
        soft_assert = SoftAssert()
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group_id_1 = create_three_grades.group_id
        stats_1 = university_service.get_grade_stats(group_id=group_id_1)

        grade_1 = create_three_grades.grade_1.grade
        grade_2 = create_three_grades.grade_2.grade
        grade_3 = create_three_grades.grade_3.grade

        list_grade = [grade_1, grade_2, grade_3]
        expected_grades_count = len(list_grade)
        expected_min_grade = min(list_grade)
        expected_max_grade = max(list_grade)
        expected_avg = (grade_1 + grade_2 + grade_3) / expected_grades_count

        soft_assert.assert_equal(stats_1.count, expected_grades_count, msg="Wrong grade count filter 'group_id'")
        soft_assert.assert_equal(stats_1.min, expected_min_grade, msg="Wrong value min grade: filter 'group_id'")
        soft_assert.assert_equal(stats_1.max, expected_max_grade, msg="Wrong value max grade: filter 'group_id'")
        soft_assert.assert_equal(stats_1.avg, expected_avg, msg="Wrong value avg grade : filter 'group_id'")
        soft_assert.check()

    def test_get_student_stats(self,
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

    def test_get_general_stats(self, university_api_utils_admin, create_and_delete_grade: GradeResponse):
        """Проверка общей статистки оценок без фильтров, где проверяется count >= 1; min, max, avg - не None"""
        university_service = UniversityService(api_utils=university_api_utils_admin)
        stats_response = university_service.get_grade_stats()
        soft_assert = SoftAssert()

        soft_assert.assert_true(stats_response.count >= 1, msg="General count grades should be >= 1")
        soft_assert.assert_not_none(stats_response.min, msg="min is None")
        soft_assert.assert_not_none(stats_response.max, msg="max is None")
        soft_assert.assert_not_none(stats_response.avg, msg="avg is None")
        soft_assert.check()

    @pytest.mark.parametrize("filter_name, id_value", [
        ("teacher_id", NONEXISTENT_ID),
        ("group_id", NONEXISTENT_ID),
        ("student_id", NONEXISTENT_ID)
    ])
    def test_stats_for_nonexistent_entity(
            self,
            university_api_utils_admin,
            filter_name,
            id_value
    ):
        """Проверка, get stats через фильтры 'teacher_id', 'group_id', 'student_id' - не существует"""
        expected_count = 0
        university_service = UniversityService(api_utils=university_api_utils_admin)

        # На бэке в фильтре можно выставить отрицательный ID
        stat_response = university_service.get_grade_stats(**{filter_name: id_value})
        soft_assert = SoftAssert()

        expected_value_grade = None

        soft_assert.assert_equal(stat_response.count, expected_count,
                                 msg=f"Wrong count grade, should be 0 from '{filter_name}'='{id_value}'")
        soft_assert.assert_equal(stat_response.min, expected_value_grade,
                                 msg=f"Wrong min value grade, should be None from '{filter_name}'")
        soft_assert.assert_equal(stat_response.max, expected_value_grade,
                                 msg=f"Wrong max value grade, should be None from '{filter_name}'")
        soft_assert.assert_equal(stat_response.avg, expected_value_grade,
                                 msg=f"Wrong avg value grade, should be None from '{filter_name}'")
        soft_assert.check()

    @pytest.mark.parametrize("student_idx", [0, 1])
    def test_get_avg_grades_students(
            self,
            university_api_utils_admin,
            student_factory,
            teacher_factory,
            grade_factory,
            student_idx
    ):
        count_grades = 5
        sa = SoftAssert()
        students = [student_factory() for _ in range(2)]
        teachers = [teacher_factory() for _ in range(2)]
        university_service = UniversityService(api_utils=university_api_utils_admin)
        target_student = students[student_idx]
        target_teacher = teachers[student_idx]

        grades = [grade_factory(teacher_id=target_teacher.id, student_id=target_student.id)
                  for _ in range(count_grades)]
        total_grade = sum(item.grade for item in grades)
        expected1_avg = total_grade / count_grades
        stats_student = university_service.get_grade_stats(student_id=target_student.id)

        sa.assert_equal(stats_student.avg, expected1_avg,
                        msg=f"For a student with id: '{target_student.id}' "
                            f"actual value avg: '{stats_student.avg}', but expected: '{expected1_avg}'")

    def test_get_avg_grades_groups(
            self,
            university_api_utils_admin,
            student_factory,
            teacher_factory,
            grade_factory
    ):
        count_grades = 5
        sa = SoftAssert()
        students = [student_factory() for i in range(2)]
        teachers = [teacher_factory() for i in range(2)]
        university_service = UniversityService(api_utils=university_api_utils_admin)
        student1_id = students[0].id
        student2_id = students[1].id
        teacher1_id = teachers[0].id
        teacher2_id = teachers[1].id
        group1_id = students[0].group_id
        group2_id = students[1].group_id

        grades1 = [grade_factory(teacher_id=teacher1_id, student_id=student1_id) for i in range(count_grades)]
        total_grade1 = sum(item.grade for item in grades1)
        expected1_avg = total_grade1 / count_grades
        stats1_student1 = university_service.get_grade_stats(student_id=student1_id)

        grades2 = [grade_factory(teacher_id=teacher2_id, student_id=student2_id) for i in range(count_grades)]
        total_grade2 = sum(item.grade for item in grades2)
        expected2_avg = total_grade2 / count_grades
        stats2_student2 = university_service.get_grade_stats(student_id=student2_id)

        stats1_group1 = university_service.get_grade_stats(group_id=group1_id)
        stats2_group2 = university_service.get_grade_stats(group_id=group2_id)

        sa.assert_equal(stats1_group1.avg, expected1_avg,
                        msg=f"For a group with id: '{group1_id}' "
                            f"actual value avg: '{stats1_student1.avg}', but expected: '{expected1_avg}'")
        sa.assert_equal(stats2_group2.avg, expected2_avg,
                        msg=f"For a group with id: '{group2_id}' "
                            f"actual value avg: '{stats2_student2.avg}', but expected: '{expected2_avg}'")
        sa.check()
