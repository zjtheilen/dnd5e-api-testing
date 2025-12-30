import pytest
from api_client import get_monster, assert_monster_schema

@pytest.mark.parametrize("monster", [
    "aboleth",
    "archmage",
    "bugbear",
    "drow"
])
def test_valid_class_schema(monster):
    response = get_monster(monster)
    assert response.status_code == 200
    data = response.json()
    assert_monster_schema(data=data)


