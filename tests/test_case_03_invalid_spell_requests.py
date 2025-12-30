import pytest
from helper import get_spell

@pytest.mark.parametrize("invalid_spell", [
    "invalid",
    "1234",
    "wizard123",
    " fireball",
])
def test_invalid_spell_returns_404(invalid_spell):
    response = get_spell(spell_index=invalid_spell)
    
    assert response.status_code == 404
    assert response.text.strip() == "Not Found"
