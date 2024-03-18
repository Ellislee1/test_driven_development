from unittest.mock import patch, Mock
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from src.weatherForecast import WeatherForecast


@patch("src.weatherForecast.requests.get")
def test_get_current_temperature(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"temperature": 20.3}
    mock_get.return_value = mock_response

    weather_forecast = WeatherForecast(api_key="abc123")

    temperature = weather_forecast.get_current_temperature("Munich")
    assert temperature == 20.3

    expected_url = "https://api.weather.com/current?city=Munich&apiKey=abc123"
    mock_get.assert_called_once_with(expected_url)


@patch("src.weatherForecast.requests.get")
def test_get_weather_conditions(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"conditions": "Sunny"}
    mock_get.return_value = mock_response

    weather_forecast = WeatherForecast(api_key="abc123")

    condition = weather_forecast.get_weather_conditions("Munich")
    assert condition == "Sunny"

    expected_url = "https://api.weather.com/conditions?city=Munich&apiKey=abc123"
    mock_get.assert_called_once_with(expected_url)
