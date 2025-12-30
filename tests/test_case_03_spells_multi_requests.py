import pytest
import requests

BASE_URL = "https://www.dnd5eapi.co/api"

@pytest.mark.parametrize("invalid_spell", [
    "invalid",
    "1234",
    "wizard123",
    " fireball",
])
def test_spells_multi_requests(invalid_spell):
    response = requests.get(f"{BASE_URL}/spells/{invalid_spell}")

    assert response.status_code == 404
    assert response.headers["Content-Type"].startswith("text/plain")
    assert response.text == "Not Found"