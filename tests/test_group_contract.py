import pytest
from faker.proxy import Faker
import requests.status_codes

from services.univesity.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContract:
    @pytest.mark.xfail(reason="BUG#2: expected status code 401, but actual 403")
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": faker.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: '{response.status_code}',"
             f" but expected: {requests.status_codes.codes.unauthorized}")
