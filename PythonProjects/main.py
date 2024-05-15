import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "USER_LOGIN",
    "password": "USER_PASSWORD"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Lichhh",
    "photo": "https://dolnikov.ru/pokemons/albums/011.png"
}
body_change = {
    "pokemon_id": "27394",
    "name": "Lich",
    "photo": "https://dolnikov.ru/pokemons/albums/011.png"
}
body_pokeball = {
    "pokemon_id": "27394"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message) //////////все что выше из лекции для отработки было'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change_name.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_add_pokeball.text) 
