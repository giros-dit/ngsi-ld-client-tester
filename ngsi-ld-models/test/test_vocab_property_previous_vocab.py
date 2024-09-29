# coding: utf-8

"""
    Example schemas for IoT device with temperature and humidity sensors and for vehicles.

    Example schemas compliant with the NGSI-LD OAS metamodel according to ETSI GS CIM 009. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.vocab_property_previous_vocab import VocabPropertyPreviousVocab

class TestVocabPropertyPreviousVocab(unittest.TestCase):
    """VocabPropertyPreviousVocab unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VocabPropertyPreviousVocab:
        """Test VocabPropertyPreviousVocab
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VocabPropertyPreviousVocab`
        """
        model = VocabPropertyPreviousVocab()
        if include_optional:
            return VocabPropertyPreviousVocab(
            )
        else:
            return VocabPropertyPreviousVocab(
        )
        """

    def testVocabPropertyPreviousVocab(self):
        """Test VocabPropertyPreviousVocab"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
