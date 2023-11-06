# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Attribute(BaseModel):
    """
    5.2.28 This type represents the data needed to define the attribute information.   # noqa: E501
    """
    id: StrictStr = Field(description="Full URI of attribute name. ")
    type: StrictStr = Field(description="JSON-LD @type. ")
    attribute_name: StrictStr = Field(description="Name of the attribute, short name if contained in @context. ", alias="attributeName")
    attribute_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of attribute instances with this attribute name. ", alias="attributeCount")
    attribute_types: Optional[List[StrictStr]] = Field(default=None, description="List of attribute types (e.g. Property, Relationship, GeoProperty) for which entity instances exist, which contain an attribute with this name. ", alias="attributeTypes")
    type_names: Optional[List[StrictStr]] = Field(default=None, description="List of entity type names for which entity instances exist containing attributes that have the respective name. ", alias="typeNames")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "attributeName", "attributeCount", "attributeTypes", "typeNames"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Attribute'):
            raise ValueError("must be one of enum values ('Attribute')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Attribute from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of Attribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "attributeName": obj.get("attributeName"),
            "attributeCount": obj.get("attributeCount"),
            "attributeTypes": obj.get("attributeTypes"),
            "typeNames": obj.get("typeNames")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


