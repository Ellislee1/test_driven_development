import requests


class WeatherForecast:
    def __init__(self, api_key: str):
        self.api_key: str = api_key
        self.base_url: str = "https://api.weather.com"

    def get_current_temperature(self, city: str) -> float:
        url: str = f'{self.base_url}/current?city={city}&apiKey={self.api_key}'

        response = requests.get(url)
        data: dict = response.json()
        return data['temperature']

    def get_weather_conditions(self, city: str) -> str:
        url: str = f'{self.base_url}/conditions?city={city}' + \
            f'&apiKey={self.api_key}'

        response = requests.get(url)
        data: dict = response.json()
        return data['conditions']
