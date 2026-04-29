import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = '/students'
    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    ID_PREFIX = ENDPOINT_PREFIX + "/{}/"

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response
    
    def delete_student(self, student_id) -> requests.Response:
        response = self.api_utils.delete(self.ID_PREFIX.format(student_id))
        return response

    def put_student(self, student_id, json: dict) -> requests.Response:
        response = self.api_utils.put(self.ID_PREFIX.format(student_id), json=json)
        return response

    def get_student(self, student_id) -> requests.Response:
        response = self.api_utils.get(self.ID_PREFIX.format(student_id))
        return response
