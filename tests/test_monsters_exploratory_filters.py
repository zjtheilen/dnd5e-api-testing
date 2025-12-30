import pytest
from api_client import get_monster

@pytest.mark.parametrize("params", [
    {"unexpected": "test"},
    {"level": "999"},
    {"name": ""},
    {"random_param": "dragon"}
])
def test_monsters_endpoint_handles_unexpected_parameters(params):
    response = get_monster(params=params)

    assert response.status_code == 200

    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)