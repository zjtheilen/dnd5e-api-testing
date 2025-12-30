import pytest
from api_client import get_class, assert_class_schema

@pytest.mark.parametrize("class_index, expected_name", [
    ("wizard", "Wizard"),
    ("bard", "Bard"),
    ("fighter", "Fighter"),
    ("cleric", "Cleric"),
])
def test_classes_valid(class_index, expected_name):
    response = get_class(class_index)
    assert response.status_code == 200

    data = response.json()
    assert_class_schema(data)
    assert data["name"] == expected_name
