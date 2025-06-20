import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = '9ff1c811f5a9769c14ca0a6c815032a9'
header = {'content-Type' : 'application/json', 'trainer_token':token}

body_registration = {
    "trainer_token": token,
    "email": "wanteruga01@yandex.ru",
    "password": "Z14ag61c"
}

body_confirmation = {
    "trainer_token": token
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

# response = requests.post(url = f'{URL}/trainers/reg', headers =  header, json = body_registration)
#print(response.text)

#response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers =  header, json = body_confirmation)
#print(response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons', headers =  header, json = body_create)
print(response_create.text)
print(response_create.status_code)

message = response_create.json()['message']
print(message)
