import requests
import pytest

token = '694d32cf1895d8ca0a3d6a586bf6ecb7'
host = 'https://api.pokemonbattle.me:9104' 

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {"trainer_id": 2620})
    assert response.status_code == 200 

def test_part_of_answer(): 
        response = requests.get(f'{host}/trainers', params = {"trainer_id": 2620})
        assert response.json()['trainer_name'] == 'Vitamin'

@pytest.mark.parametrize('key,value', [('city', 'tokyo')
                                       ('trainer_name', 'vitamin')])


def test_part_of_answer(key, value):
      response = requests.get(f'{host}/pokemons', params = {"trainer_id": 2620})
      assert response.json()['key'] == value
      