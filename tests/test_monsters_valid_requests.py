import pytest
from api_client import get_monster, assert_monster_schema

@pytest.mark.parametrize("monster_index, expected_name", [
    ("aboleth", "Aboleth"),
    ("archmage", "Archmage"),
    ("bugbear", "Bugbear"),
    ("drow", "Drow"),
])
def test_monsters_valid(monster_index, expected_name):
    response = get_monster(monster_index)
    assert response.status_code == 200

    data = response.json()
    assert_monster_schema(data)
    assert data["name"] == expected_name
