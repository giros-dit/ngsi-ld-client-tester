import sys
import os
import json
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import unittest

from ngsi_ld_models.models.iot_device import IotDevice
from ngsi_ld_models.models.temperature_sensor import TemperatureSensor
from ngsi_ld_models.models.humidity_sensor import HumiditySensor

class IotSensors(unittest.TestCase):
    def test_iot_device(self):
        json_file = open("examples/iot-device/example-normalized.json")
        self.assertIsInstance(
            IotDevice.model_validate(json.load(json_file)),
            IotDevice)
        json_file.close()
    def test_temperature_sensor(self):
        json_file = open("examples/temperature-sensor/example-normalized.json")
        self.assertIsInstance(
            TemperatureSensor.model_validate(json.load(json_file)),
            TemperatureSensor)
        json_file.close()
    def test_humidity_sensor(self):
        json_file = open("examples/humidity-sensor/example-normalized.json")
        self.assertIsInstance(
            HumiditySensor.model_validate(json.load(json_file)),
            HumiditySensor)
        json_file.close()

if __name__ == '__main__':
    unittest.main()