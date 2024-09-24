# coding: utf-8

"""
    Example schemas for IoT device with temperature and humidity sensors

    Example schemas compliant with the NGSI-LD OAS metamodel according to ETSI GS CIM 009. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.relationship_previous_object import RelationshipPreviousObject

class TestRelationshipPreviousObject(unittest.TestCase):
    """RelationshipPreviousObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelationshipPreviousObject:
        """Test RelationshipPreviousObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelationshipPreviousObject`
        """
        model = RelationshipPreviousObject()
        if include_optional:
            return RelationshipPreviousObject(
            )
        else:
            return RelationshipPreviousObject(
        )
        """

    def testRelationshipPreviousObject(self):
        """Test RelationshipPreviousObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
