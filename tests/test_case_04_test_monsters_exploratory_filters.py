import requests
import pytest

BASE_URL = "https://www.dnd5eapi.co/api"

@pytest.mark.parametrize("params", [
    {"unexpected": "test"},
    {"level": "999"},
    {"name": ""},
    {"random_param": "dragon"}
])
def test_monsters_endpoint_handles_unexpected_parameters(params):
    response = requests.get(f"{BASE_URL}/monsters", params=params)

    assert response.status_code == 200

    # should still see a valid JSON
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)