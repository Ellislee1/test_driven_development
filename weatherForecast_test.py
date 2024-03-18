import unittest
from unittest.mock import patch, Mock
from src.weatherForecast import WeatherForecast


class TestWeatherForecast(unittest.TestCase):

    @patch('src.weatherForecast.requests.get')
    def test_get_current_temperature(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'temperature': 20.3}
        mock_get.return_value = mock_response

        weather_forecast = WeatherForecast(api_key="abc123")

        temperature = weather_forecast.get_current_temperature("Munich")
        self.assertEquals(temperature, 20.3)

        expected_url = "https://api.weather.com/current?city=Munich&" + \
            "apiKey=abc123"
        mock_get.assert_called_once_with(expected_url)

    @patch('src.weatherForecast.requests.get')
    def test_get_weather_conditions(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'conditions': 'Sunny'}
        mock_get.return_value = mock_response

        weather_forecast = WeatherForecast(api_key="abc123")

        condition = weather_forecast.get_weather_conditions("Munich")
        self.assertEquals(condition, 'Sunny')

        expected_url = "https://api.weather.com/conditions?city=Munich&" + \
            "apiKey=abc123"
        mock_get.assert_called_once_with(expected_url)


if __name__ == '__main__':
    unittest.main()
