import requests
from services.univesity.helpers.grade_helper import GradeHelper
from services.univesity.models.grade_stats_request import GradeStatsRequest


class GradeStatsHelper(GradeHelper):
    ENDPOINT_PREFIX = GradeHelper.ENDPOINT_PREFIX + '/stats'

    def get_grades_stats(self, grade_stats: GradeStatsRequest = None) -> requests.Response:
        params = {}
        if grade_stats:
            params = grade_stats.model_dump(exclude_none=True)
        params = {k: v for k, v in params.items() if v is not None}
        response = self.api_utils.get(self.ENDPOINT_PREFIX, params=params)
        return response
