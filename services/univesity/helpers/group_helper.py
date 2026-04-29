import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = '/groups'
    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    ID_PREFIX = ENDPOINT_PREFIX + "/{}/"

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def put_group(self, group_id, json) -> requests.Response:
        response = self.api_utils.put(self.ID_PREFIX.format(group_id), json=json)
        return response

    def get_group(self, group_id) -> requests.Response:
        response = self.api_utils.get(self.ID_PREFIX.format(group_id))
        return response

    def delete_group(self, group_id) -> requests.Response:
        response = self.api_utils.delete(self.ID_PREFIX.format(group_id))
        return response
