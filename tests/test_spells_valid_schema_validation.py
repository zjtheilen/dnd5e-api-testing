import pytest
from api_client import get_spell_by_index, assert_spell_schema

@pytest.mark.parametrize("spell_index, expected_level", [
    ("fireball", 3),
    ("mage-hand", 0),
    ("acid-arrow", 2)
])
def test_valid_spell_schema(spell_index, expected_level):
    response = get_spell_by_index(spell_index=spell_index)
    assert response.status_code == 200
    data = response.json()
    assert_spell_schema(data=data)
