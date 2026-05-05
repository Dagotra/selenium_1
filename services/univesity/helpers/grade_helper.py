import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = '/grades'
    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    ID_GRADE = ENDPOINT_PREFIX + "/{}/"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def delete_grade(self, grade_id) -> requests.Response:
        response = self.api_utils.delete(self.ID_GRADE.format(grade_id))
        return response

    def put_grade(self, grade_id, json: dict) -> requests.Response:
        response = self.api_utils.put(self.ID_GRADE.format(grade_id), json=json)
        return response

    def get_grade(self, grade_id) -> requests.Response:
        response = self.api_utils.get(self.ID_GRADE.format(grade_id))
        return response
