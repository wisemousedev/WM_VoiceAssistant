import requests
import json

from settings import HA_API_KEY

base_url = 'https://homeassistant.local:8123/api/'
headers = {
    'Authorization': f'Bearer {HA_API_KEY}',
    'content-type': 'application/json',
}
def checkMainLight():
    # Get the state of an entity
    entity_id = 'light.living_room_pendants'
    response = requests.get(
        f'{base_url}states/{entity_id}',
        headers=headers,
        verify=False
    )
    print(response.text)

def turnOnMainLivingRoomLight():
    # Turn on a light
    entity_id = 'light.living_room_pendants'
    data = {"entity_id": entity_id}
    response = requests.post(
        f'{base_url}services/light/turn_on',
        headers=headers,
        data=json.dumps(data),
        verify=False
    )
    print(response.text)

def turnOfMainLivingRoomLight():
    # Turn off a light
    entity_id = 'light.living_room_pendants'
    data = {"entity_id": entity_id}
    response = requests.post(
        f'{base_url}services/light/turn_off',
        headers=headers,
        data=json.dumps(data),
        verify=False
    )
    print(response.text)

def turnTVLight():
    # Turn on a light
    entity_id = 'light.main_lvl_living_tv'
    data = {"entity_id": entity_id}
    response = requests.post(
        f'{base_url}services/light/turn_on',
        headers=headers,
        data=json.dumps(data),
        verify=False
    )
    print(response.text)
