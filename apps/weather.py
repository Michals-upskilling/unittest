import requests
import json
import logging as log

log.getLogger().setLevel(log.INFO)


class WeatherForecast(object):
    """
    Weather Forecast general class
    """

    URL = "http://api.openweathermap.org/data/2.5/weather"
    APPID = "XXX"

    def __init__(self, url: str = URL, units: str = "metric") -> None:
        self.url = url
        self.units = units

    def __str__(self) -> str:
        return f"WeatherForecast(url={self.url}, units={self.units})"

    def get_forecast(self, city: str) -> json:
        """
        Retrieve weather forecast for city
        """
        try:
            log.info("Retrieving forecast for %s", city)
            params = {
                "q": city,
                "units": self.units,
                "appid": WeatherForecast.APPID,
            }
            headers = {"Content-type": "application/json"}
            forecast = requests.get(
                url=WeatherForecast.URL, params=params, headers=headers
            ).json()
            log.info("Forecast data for %s: %s", city, forecast)

            return forecast
        except Exception as err:
            log.error(f"Exception: {err}")
            return {}


class TemperatureForecast(WeatherForecast):
    def __init__(self) -> None:
        super(TemperatureForecast, self).__init__()

    def __str__(self) -> str:
        return f"TemperatureForecast({super(TemperatureForecast, self).__str__()})"

    def get_temperature(self, city: str) -> int:
        try:
            log.info(f"Retrieving temperature for: {city}...")
            return self.get_forecast(city)["main"]["temp"]
        except KeyError as err:
            log.error(f"KeyError: {err}")
            return None
