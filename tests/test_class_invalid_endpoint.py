from api_client import get_class

BASE_URL = "https://www.dnd5eapi.co/api"

def test_invalid_class_endpoint():
    response = get_class("invalid")

    assert response.status_code == 404
    assert response.headers["Content-Type"].startswith("text/plain")
    assert response.text == "Not Found"
