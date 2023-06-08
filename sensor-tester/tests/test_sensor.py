import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import unittest

from ngsi_ld_client.models.sensor import Sensor

class Sensors(unittest.TestCase):
    def test_interface(self):
        self.assertIsInstance(
            Sensor.parse_file(
                "example/example-normalized.json"),
            Sensor)

if __name__ == '__main__':
    unittest.main()