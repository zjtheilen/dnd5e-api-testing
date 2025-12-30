# helper.py
import requests

BASE_URL = "https://www.dnd5eapi.co/api"

def get_spell(spell_index):
    return requests.get(f"{BASE_URL}/spells/{spell_index}")

def get_class(class_name):
    return requests.get(f"{BASE_URL}/classes/{class_name}")

def get_monster(params=None):
    return requests.get(f"{BASE_URL}/monsters/", params=params)