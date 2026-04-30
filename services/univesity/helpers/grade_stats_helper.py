import requests
from services.univesity.helpers.grade_helper import GradeHelper
from services.univesity.models.grade_stats_request import GradeStatsRequest


class GradeStatsHelper(GradeHelper):
    ENDPOINT_PREFIX = GradeHelper.ENDPOINT_PREFIX + '/stats'

    def get_grades_stats(self, grade_stats: GradeStatsRequest = None) -> requests.Response:
        params = {}
        if grade_stats:
            if grade_stats.student_id is not None:
                params["student_id"] = grade_stats.student_id
            if grade_stats.teacher_id is not None:
                params["teacher_id"] = grade_stats.teacher_id
            if grade_stats.group_id is not None:
                params["group_id"] = grade_stats.group_id
        params = {k: v for k, v in params.items() if v is not None}
        response = self.api_utils.get(self.ENDPOINT_PREFIX, params=params)
        return response
