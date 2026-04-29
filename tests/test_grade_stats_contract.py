import pytest
import requests.status_codes
from services.univesity.helpers.grade_stats_helper import GradeStatsHelper
from services.univesity.models.grade_response import GradeResponse


class TestGradeStatsContract:
    def test_stats_grade_admin(
            self,
            university_api_utils_admin,
            create_and_delete_grade: GradeResponse
    ):
        stats_helper = GradeStatsHelper(api_utils=university_api_utils_admin)
        response = stats_helper.get_grades_stats()
        assert response.status_code == requests.status_codes.codes.ok,  \
            (f"Wrong status code. Actual: '{response.status_code}',"
             f" but expected: {requests.status_codes.codes.ok}")

    @pytest.mark.xfail(reason="BUG#1: expected status code 401, but actual 403")
    def test_stats_grade_anonym(
            self,
            university_api_utils_anonym,
            create_and_delete_grade: GradeResponse
    ):
        stats_helper = GradeStatsHelper(api_utils=university_api_utils_anonym)
        response = stats_helper.get_grades_stats()

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: '{response.status_code}',"
             f" but expected: {requests.status_codes.codes.unauthorized}")
