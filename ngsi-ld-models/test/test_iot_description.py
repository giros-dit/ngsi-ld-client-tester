# coding: utf-8

"""
    Example schemas for IoT device with temperature and humidity sensors and for vehicles.

    Example schemas compliant with the NGSI-LD OAS metamodel according to ETSI GS CIM 009. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.iot_description import IotDescription

class TestIotDescription(unittest.TestCase):
    """IotDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IotDescription:
        """Test IotDescription
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IotDescription`
        """
        model = IotDescription()
        if include_optional:
            return IotDescription(
                type = 'Property',
                value = '',
                observed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                unit_code = '',
                dataset_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                instance_id = '',
                previous_value = None
            )
        else:
            return IotDescription(
                value = '',
        )
        """

    def testIotDescription(self):
        """Test IotDescription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
