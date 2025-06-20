import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
token = 'ТОКЕН_ТРЕНЕРА' # указать токен тренера
header = {'content-Type' : 'application/json', 'trainer_token':token}
trainer_id = '35816'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'sort' : 'desc_level'})
    assert response.status_code == 200

def test_trainer_info():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id})
    assert response_get.json()["data"][0]['id'] == trainer_id
