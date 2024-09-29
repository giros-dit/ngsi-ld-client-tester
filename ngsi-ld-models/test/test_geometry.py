# coding: utf-8

"""
    Example schemas for IoT device with temperature and humidity sensors and for vehicles.

    Example schemas compliant with the NGSI-LD OAS metamodel according to ETSI GS CIM 009. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.geometry import Geometry

class TestGeometry(unittest.TestCase):
    """Geometry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Geometry:
        """Test Geometry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Geometry`
        """
        model = Geometry()
        if include_optional:
            return Geometry(
                type = 'Point',
                coordinates = [
                    ngsi_ld_models.models.geometry/line_string.Geometry.LineString(
                        type = 'LineString', )
                    ]
            )
        else:
            return Geometry(
        )
        """

    def testGeometry(self):
        """Test Geometry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
