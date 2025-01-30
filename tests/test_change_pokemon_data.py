import requests
import pytest

HOST = 'https://api.pokemonbattle.ru'
VERSION = '/v2'
TRAINERS = '/trainers'
ADD_POKEBALL = '/add_pokeball'
POKEMONS = '/pokemons'
KNOCKOUT = '/knockout'
ME = '/me'

HEADERS = {
    'Content-type' : 'application/json',
    'trainer_token' : 'db330d6d6484ddfd5b23b8fc1e4005b1'
}

create_pokemon_data = {
    "name": "generate",
    "photo_id": 1
}
@pytest.fixture()
def create_pokemon():
    response = requests.post(
                    url = f"{HOST}{VERSION}{POKEMONS}",
                    headers = HEADERS,
                    json = create_pokemon_data
                )
    print(response.json()['id'])
    return {
        "pokemon_id": response.json()['id'],
        "message": response.json()['message'],
        "name": "тест",
        "photo_id": 1
    }

def test_create_new_pokemon(create_pokemon):
    assert create_pokemon.get('message') == 'Покемон создан'

def test_catch_pokemon_in_pokeball(create_pokemon):
    response = requests.post(
                    url = f"{HOST}{VERSION}{TRAINERS}{ADD_POKEBALL}",
                    headers = HEADERS,
                    json = create_pokemon
                )
    assert response.status_code == 200
    assert response.json()['message'] == 'Покемон пойман в покебол'

def test_change_pokemon_name(create_pokemon):
    response = requests.put(
                    url = f"{HOST}{VERSION}{POKEMONS}",
                    headers = HEADERS,
                    json ={**create_pokemon, "name": "тест", "photo_id": 1}
                )
    print(response.json())
    assert response.status_code == 200
    assert response.json()['message'] == 'Информация о покемоне обновлена'