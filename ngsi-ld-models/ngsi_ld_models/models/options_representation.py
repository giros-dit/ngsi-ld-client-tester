# coding: utf-8

"""
    NGSI-LD metamodel and Sensor NGSI-LD custom model

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API; NGSI-LD metamodel and Sensor NGSI-LD custom model.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class OptionsRepresentation(str, Enum):
    """
    6.3.7 Representation of Entities. When its value includes the keyword \"normalized\", a normalized representation of Entities shall be provided as defined by clause 4.5.1, with Attributes returned in the normalized representation as defined in clauses 4.5.2.2, 4.5.3.2 and 4.5.18.2.  When its value includes the keyword \"concise\", a concise lossless representation of Entities shall be provided as defined by clause 4.5.1. with Attributes returned in the concise representation as defined in clauses 4.5.2.3, 4.5.3.3 and 4.5.18.3. In this case the broker will return data in the most concise lossless representation possible, for example removing all Attribute \"type\" members.  When its value includes the keyword \"keyValues\" (or \"simplified\" as a synonym), a simplified representation of Entities shall be provided as defined by clause 4.5.4.  If the Accept Header is set to \"application/geo+json\" the response will be in simplified GeoJSON format as defined by clause 4.5.17. 
    """

    """
    allowed enum values
    """
    NORMALIZED = 'normalized'
    CONCISE = 'concise'
    KEYVALUES = 'keyValues'

    @classmethod
    def from_json(cls, json_str: str) -> OptionsRepresentation:
        """Create an instance of OptionsRepresentation from a JSON string"""
        return OptionsRepresentation(json.loads(json_str))


