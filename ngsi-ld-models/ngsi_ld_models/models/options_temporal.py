# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class OptionsTemporal(str, Enum):
    """
    6.3.12 Simplified or aggregated temporal representation of entities.  When its value includes the keyword \"temporalValues\", a simplified temporal representation of entities shall be provided as defined by clause 4.5.8.  When its value includes the keyword \"aggregatedValues\", an aggregated temporal representation of entities shall be provided as defined by clause 4.5.19.  Only one of the two keywords can be present in the values of the parameter. 
    """

    """
    allowed enum values
    """
    TEMPORALVALUES = 'temporalValues'
    AGGREGATEDVALUES = 'aggregatedValues'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OptionsTemporal from a JSON string"""
        return cls(json.loads(json_str))


