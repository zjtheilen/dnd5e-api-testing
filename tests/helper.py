import requests

BASE_URL = "https://www.dnd5eapi.co/api"

def get_spell_by_index(spell_index=None, params=None):
    if spell_index:
        return requests.get(f"{BASE_URL}/spells/{spell_index}")
    return requests.get(f"{BASE_URL}/spells", params=params)

def get_class(class_name):
    return requests.get(f"{BASE_URL}/classes/{class_name}")

def get_monster(params=None):
    return requests.get(f"{BASE_URL}/monsters/", params=params)

def assert_spell_schema(data):
    assert isinstance(data, dict)
    assert "index" in data
    assert "name" in data
    assert "level" in data
    assert isinstance(data["name"], str)
    assert isinstance(data["level"], int)