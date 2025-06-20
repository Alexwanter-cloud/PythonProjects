import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
token = '9ff1c811f5a9769c14ca0a6c815032a9'
header = {'content-Type' : 'application/json', 'trainer_token':token}
trainer_id = '35816'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : trainer_id})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : trainer_id})
    assert response_get.json()["data"][0]['name'] == 'Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', trainer_id), ('id', '340219')])
def test_parametrize(key, value ):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : trainer_id})
    assert response_parametrize.json()["data"][0][key] == value