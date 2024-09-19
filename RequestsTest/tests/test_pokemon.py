import requests

import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 3585})
    assert response.status_code == 200

def test_part_of_body():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 3585})
    assert response.json()["trainer_name"] == "Vovch1k"

@pytest.mark.parametrize('key, value', [("trainer_name", "Vovch1k"),
                                        ("id", "3585"), 
                                        ("city", "Saint-P")])
def test_response_json(key, value):
    response = requests.get(f'{host}/trainers', params={'trainer_id':3585})
    assert response.json()[key]  == value