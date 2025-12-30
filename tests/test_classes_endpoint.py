from api_client import get_class

BASE_URL = "https://www.dnd5eapi.co/api"

def test_classes_endpoint():
    response = get_class("")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)
