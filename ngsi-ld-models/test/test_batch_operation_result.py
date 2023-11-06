# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from ngsi_ld_models.models.batch_operation_result import BatchOperationResult  # noqa: E501

class TestBatchOperationResult(unittest.TestCase):
    """BatchOperationResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchOperationResult:
        """Test BatchOperationResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchOperationResult`
        """
        model = BatchOperationResult()  # noqa: E501
        if include_optional:
            return BatchOperationResult(
                success = [
                    ''
                    ],
                errors = [
                    ngsi_ld_models.models.batch_entity_error.BatchEntityError(
                        entity_id = '', 
                        registration_id = '', 
                        error = ngsi_ld_models.models.problem_details.ProblemDetails(
                            type = '', 
                            title = '', 
                            status = 56, 
                            detail = '', 
                            instance = '', ), )
                    ]
            )
        else:
            return BatchOperationResult(
                success = [
                    ''
                    ],
        )
        """

    def testBatchOperationResult(self):
        """Test BatchOperationResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
