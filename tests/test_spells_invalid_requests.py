import pytest
from api_client import get_spell_by_index, assert_spell_schema

@pytest.mark.parametrize("invalid_spell", [
    "invalid",
    "1234",
    "wizard123",
    " fireball",
])
def test_spells_endpoint_returns_404_for_invalid_spell_index(invalid_spell):
    response = get_spell_by_index(spell_index=invalid_spell)
    
    assert response.status_code == 404
    assert response.text.strip() == "Not Found"
