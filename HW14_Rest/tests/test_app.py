# from config import Config
#
#
# def test_homepage(client):
#
#     responce = client.get("/")
#     assert responce.status_code == 200
#
# def test_search_weather(client):
#     Config.WEATHER_API_KEY = "e8690fbba9msh1209a7decfafc6ep18f808jsn53b7428c1268"
#     Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
#     Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
#     response = client.post("/search", data={"cities":"london"})
#     assert response.status_code == 200
#     assert b"Weather for London" in response.data
#
#
#
# def test_search_weather_mock(client, mocker):
#     mocker.patch('requests.request', side_effect=ApiMock)
#     responce = client.post("/search", data={"cities": "Kyiv"})
#     assert responce.status_code == 200
#     assert b"Weather for Kyiv" in responce.data
#
#
# class ApiMock:
#     def __init__(self, *args, **kwargs):
#         self.data = {"message": "accurate", "cod": "200", "count": "1", "list": [
#             {"id": 703448, "name": "Kyiv", "coord": {"lat": 50.4333, "lon": 30.5167},
#              "main": {"temp": 25.27, "feels_like": 25.24, "temp_min": 25, "temp_max": 26, "pressure": 1013,
#                       "humidity": 53}, "dt": 1623676150, "wind": {"speed": 3, "deg": 90},
#              "sys": {"country": "UA"}, "rain": None, "snow": None, "clouds": {"all": 40},
#              "weather": [{"id": 802, "main": "Clouds", "description": "scattered clouds", "icon": "03d"}]}]}
#         self.status_code = 200
#
#     def json(self):
#         return self.data
