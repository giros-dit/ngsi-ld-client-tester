# coding: utf-8

"""
    NGSI-LD metamodel and Sensor NGSI-LD custom model

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API; NGSI-LD metamodel and Sensor NGSI-LD custom model.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import ngsi_ld_models
from ngsi_ld_models.models.registration_info import RegistrationInfo  # noqa: E501
from ngsi_ld_models.rest import ApiException

class TestRegistrationInfo(unittest.TestCase):
    """RegistrationInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegistrationInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegistrationInfo`
        """
        model = ngsi_ld_models.models.registration_info.RegistrationInfo()  # noqa: E501
        if include_optional :
            return RegistrationInfo(
                entities = [
                    ngsi_ld_models.models.entity_info.EntityInfo(
                        id = '', 
                        id_pattern = '', 
                        type = null, )
                    ], 
                property_names = [
                    ''
                    ], 
                relationship_names = [
                    ''
                    ]
            )
        else :
            return RegistrationInfo(
        )
        """

    def testRegistrationInfo(self):
        """Test RegistrationInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
