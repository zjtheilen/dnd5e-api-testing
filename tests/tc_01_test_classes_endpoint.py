import requests

BASE_URL = "https://www.dnd5eapi.co/api"

def test_classes_endpoint():
    response = requests.get(f"{BASE_URL}/classes")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)
