import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = 'ТОКЕН_ТРЕНЕРА' # указать токен тренера
header = {'content-Type' : 'application/json', 'trainer_token':token}

body_create = {
    "name": "{{$randomFirstName}}",
    "photo_id": 12
}

response_create = requests.post(url = f'{URL}/pokemons', headers =  header, json = body_create)
print("\033[92mBody response:\033[0m", response_create.text)
print("\033[92mКод ответа сервера:\033[0m", response_create.status_code)
response_data = response_create.json()
pokemon_id = response_data['id']

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

response_rename = requests.put(url = f'{URL}/pokemons', headers =  header, json = body_rename)
print("\033[92mBody response:\033[0m", response_rename.text)
print("\033[92mКод ответа сервера:\033[0m", response_rename.status_code)

body_add = {
    "pokemon_id": pokemon_id
}

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers =  header, json = body_add)
print("\033[92mBody response:\033[0m", response_addpokeball.text)
print("\033[92mКод ответа сервера:\033[0m", response_addpokeball.status_code)
