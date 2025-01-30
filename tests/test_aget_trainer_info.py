import requests
import pytest

HOST = 'https://api.pokemonbattle.ru'
VERSION = '/v2'
TRAINERS = '/trainers'
ME = '/me'
HEADERS = {
    'Content-type' : 'application/json',
    'trainer_token' : 'db330d6d6484ddfd5b23b8fc1e4005b1'
}
update_trainer_info_data = {
    "name": "Api testing",
    "city": "Огайоу"
}

update_part_trainer_info_data = {
    "name": "Супер"
}

def test_update_part_trainer_info():
    response = requests.patch(
        url=f"{HOST}{VERSION}{TRAINERS}",
        headers=HEADERS,
        json=update_part_trainer_info_data
    )
    assert response.status_code == 200
    assert response.json()['message'] == 'Информация о тренере обновлена'
    assert response.json()['id'] == '22149'

def test_update_trainer_info():
    response = requests.put(
        url=f"{HOST}{VERSION}{TRAINERS}",
        headers=HEADERS,
        json=update_trainer_info_data
    )
    assert response.status_code == 200
    assert response.json()['message'] == 'Информация о тренере обновлена'
    assert response.json()['id'] == '22149'



@pytest.mark.parametrize('key, value', [
    ('id', '22149'),
    ('is_premium', False),
    ('avatar_id', 10)
], )

def test_get_info_about_trainer(key, value):
    response = requests.get(
        url=f"{HOST}{VERSION}{ME}",
        headers=HEADERS
    )
    assert response.json()['data'][0][key] == value

