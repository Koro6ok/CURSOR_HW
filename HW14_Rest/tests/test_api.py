from tests.conftest import client, todos
import json
from config import Config


def test_create(client, todos):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post("/todos", headers=headers, json=todos)
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_list(client):
    responce = client.get('/todos')
    assert responce.status_code == 200
    assert responce.json['1'] == "text"


def test_update(client):
    update_data = {
        "text": "blabla"
    }

    responce = client.put("/todos/1", json=update_data)
    assert responce.status_code == 200
    get_responce = client.get("/todos/1")
    assert get_responce.status_code == 200
    assert get_responce.json['1'] == "blabla"

def test_delete(client):
    responce = client.delete("/todos/1")
    assert responce.status_code == 204
    responce = client.get("/todos/1")
    assert responce.status_code == 404


def test_weather(client):
    Config.WEATHER_API_KEY = "e8690fbba9msh1209a7decfafc6ep18f808jsn53b7428c1268"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.get('/weather?city=Kyiv')
    assert response.status_code == 200
    response = client.get('/weather?city=Lviv,London')
    assert response.status_code == 200