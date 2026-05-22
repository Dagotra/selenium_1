import requests
from services.univesity.helpers.grade_helper import GradeHelper


class GradeStatsHelper(GradeHelper):
    ENDPOINT_PREFIX = GradeHelper.ENDPOINT_PREFIX + '/stats'

    def get_grades_stats(
            self,
            student_id: int | None = None,
            teacher_id: int | None = None,
            group_id: int | None = None
    ) -> requests.Response:
        params = {}
        if student_id is not None:
            params["student_id"] = student_id
        if teacher_id is not None:
            params["teacher_id"] = teacher_id
        if group_id is not None:
            params["group_id"] = group_id
        response = self.api_utils.get(self.ENDPOINT_PREFIX, params=params)
        return response
