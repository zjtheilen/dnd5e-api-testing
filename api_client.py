import requests

BASE_URL = "https://www.dnd5eapi.co/api"

def get_spell_by_index(spell_index=None, params=None):
    if spell_index:
        return requests.get(f"{BASE_URL}/spells/{spell_index}")
    return requests.get(f"{BASE_URL}/spells", params=params)

def get_class(class_name):
    return requests.get(f"{BASE_URL}/classes/{class_name}")

def get_monster(monster_index=None, params=None):
    if monster_index:
        return requests.get(f"{BASE_URL}/monsters/{monster_index}")
    return requests.get(f"{BASE_URL}/monsters/", params=params)

# -------------------- Schema validation --------------------

def assert_spell_schema(data):
    assert isinstance(data, dict)
    assert "index" in data
    assert "name" in data
    assert "level" in data
    assert isinstance(data["name"], str)
    assert isinstance(data["level"], int)

def assert_class_schema(data):
    assert isinstance(data, dict)
    required_keys = ["index", "hit_die", "proficiency_choices", "proficiencies", "saving_throws"]
    for key in required_keys:
        assert key in data

    assert isinstance(data["index"], str)
    assert isinstance(data["hit_die"], int)
    assert isinstance(data["proficiencies"], list)
    assert isinstance(data["saving_throws"], list)
    assert isinstance(data["proficiency_choices"], list)


def assert_monster_schema(data):
    assert isinstance(data, dict)

    required_keys = ["index", "name", "size", "type", "alignment", "armor_class", "hit_points", "challenge_rating"]
    for key in required_keys:
        assert key in data

    assert isinstance(data["index"], str)
    assert isinstance(data["name"], str)
    assert isinstance(data["size"], str)
    assert isinstance(data["type"], str)
    assert isinstance(data["alignment"], str)

    # armor_class can be int or list of dicts
    ac = data["armor_class"]
    if isinstance(ac, int):
        pass
    elif isinstance(ac, list):
        for entry in ac:
            assert "type" in entry
            assert "value" in entry
            assert isinstance(entry["value"], int)
    else:
        raise AssertionError(f"Unexpected armor_class type: {type(ac)}")

    assert isinstance(data["hit_points"], int)
    assert isinstance(data["challenge_rating"], (int, float))

