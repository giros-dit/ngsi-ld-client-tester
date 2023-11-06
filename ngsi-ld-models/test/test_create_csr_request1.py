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

from ngsi_ld_models.models.create_csr_request1 import CreateCSRRequest1  # noqa: E501

class TestCreateCSRRequest1(unittest.TestCase):
    """CreateCSRRequest1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCSRRequest1:
        """Test CreateCSRRequest1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCSRRequest1`
        """
        model = CreateCSRRequest1()  # noqa: E501
        if include_optional:
            return CreateCSRRequest1(
                id = '',
                type = 'ContextSourceRegistration',
                registration_name = '0',
                description = '0',
                information = [
                    ngsi_ld_models.models.registration_info.RegistrationInfo(
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
                            ], )
                    ],
                tenant = '',
                observation_interval = ngsi_ld_models.models.time_interval.TimeInterval(
                    start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                management_interval = ngsi_ld_models.models.time_interval.TimeInterval(
                    start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                location = None,
                observation_space = None,
                operation_space = None,
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                endpoint = '',
                context_source_info = [
                    ngsi_ld_models.models.key_value_pair.KeyValuePair(
                        key = '', 
                        value = '', )
                    ],
                scope = None,
                mode = 'inclusive',
                operations = [
                    ''
                    ],
                refresh_rate = '',
                management = ngsi_ld_models.models.registration_management_info.RegistrationManagementInfo(
                    local_only = True, 
                    cache_duration = '', 
                    timeout = 1, 
                    cooldown = 1, ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'ok',
                times_sent = 0,
                times_failed = 0,
                last_success = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_failure = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                context = None
            )
        else:
            return CreateCSRRequest1(
                type = 'ContextSourceRegistration',
                information = [
                    ngsi_ld_models.models.registration_info.RegistrationInfo(
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
                            ], )
                    ],
                context = None,
        )
        """

    def testCreateCSRRequest1(self):
        """Test CreateCSRRequest1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
