import requests

from services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    ENDPOINT_PREFIX = '/teachers'
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    ID_PREFIX = ENDPOINT_PREFIX + "/{}/"

    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_teacher(self, teacher_id) -> requests.Response:
        response = self.api_utils.delete(self.ID_PREFIX.format(teacher_id))
        return response

    def put_teacher(self, teacher_id, json: dict) -> requests.Response:
        response = self.api_utils.put(self.ID_PREFIX.format(teacher_id), json=json)
        return response

    def get_teacher(self, teacher_id) -> requests.Response:
        response = self.api_utils.get(self.ID_PREFIX.format(teacher_id))
        return response
