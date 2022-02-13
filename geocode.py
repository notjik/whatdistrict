import requests

SERVER = 'http://geocode-maps.yandex.ru/1.x/'
API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"


def get_coord(address):
    params = {'apikey': API_KEY,
              'geocode': address,
              'format': 'json'}
    resp = requests.get(SERVER, params=params)
    if resp:
        resp = resp.json()
    else:
        raise RuntimeError('Ошибка выполнения запроса')
    return ','.join(resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split())


def geocode(coord):
    params = {'apikey': API_KEY,
                     'geocode': coord,
                     'format': 'json',
                     'kind': 'district'}
    resp = requests.get(SERVER, params=params)
    if resp:
        resp = resp.json()
    else:
        raise RuntimeError('Ошибка выполнения запроса')
    return resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
