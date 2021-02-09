import json

import pytest


@pytest.fixture()
def mock_tx():
    with open("tests/tasks/0bf7d87c-aafb-5eb7-8326-3f37d56109eb.json", encoding="utf8") as fp:
        return json.load(fp)