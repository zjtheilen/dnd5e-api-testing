import pytest
from api_client import get_class, assert_class_schema

@pytest.mark.parametrize("class_name", [
    "bard",
    "druid",
    "wizard",
    "cleric"
])
def test_valid_class_schema(class_name):
    response = get_class(class_name=class_name)
    assert response.status_code == 200
    data = response.json()
    assert_class_schema(data=data)


