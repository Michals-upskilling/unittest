import requests
import unittest

from apps.weather import WeatherForecast
from apps.weather import TemperatureForecast
from unittest import mock


class testWeatherForecast(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.mock_wf = WeatherForecast(url='test_url', units='test_units')

    @mock.patch.object(requests, 'get')
    def test_get_forecast(self,  mock_forecast):
        mock_forecast.return_value.json.return_value = 'test weateher'

        with self.assertLogs() as log:
            test_forecast = self.mock_wf.get_forecast('test City')

        self.assertEqual(test_forecast, 'test weateher')
        self.assertIn("Retrieving forecast for test City",
                      "\n".join(log.output))
        self.assertIn("Forecast data for test City: test weateher",
                      "\n".join(log.output))

    @mock.patch.object(requests, 'get', side_effect=Exception)
    def test_get_forecast_exception(self, mock_forecast):

        with self.assertLogs() as log:
            test_forecast = self.mock_wf.get_forecast('test City')

        self.assertEqual(test_forecast, {})
        self.assertIn("Exception: ",
                      "\n".join(log.output))

    def test__str__(self):
        self.assertEqual(self.mock_wf.__str__(),
                         "WeatherForecast(url=test_url, units=test_units)")


class testTemperatureForecast(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.mock_tf = TemperatureForecast()

    @mock.patch.object(WeatherForecast, 'get_forecast',
                       return_value={"main": {"temp": "test_temperature"}})
    def test_get_temperature(self, mock_forecast):

        with self.assertLogs() as log:
            test_temperature = self.mock_tf.get_temperature('test City')

        self.assertEqual(test_temperature, "test_temperature")
        self.assertIn("Retrieving temperature for: test City...",
                      "\n".join(log.output))

    @mock.patch.object(WeatherForecast, 'get_forecast', side_effect=KeyError)
    def test_get_temperatrure_KeyError(self, mock_forecast):

        with self.assertLogs() as log:
            test_temperature = self.mock_tf.get_temperature('test City')

        self.assertEqual(test_temperature, None)
        self.assertIn("KeyError: ", "\n".join(log.output))

    def test__str__(self):
        self.mock_tf.units = "test_units"
        self.mock_tf.url = 'test_url'

        self.assertEqual(self.mock_tf.__str__(),
                         "TemperatureForecast(WeatherForecast"
                         "(url=test_url, units=test_units))")
