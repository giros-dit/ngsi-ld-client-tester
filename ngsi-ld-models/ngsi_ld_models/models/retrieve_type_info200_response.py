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


from typing import Any, ClassVar, Dict, List, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from ngsi_ld_models.models.attribute import Attribute
from ngsi_ld_models.models.ld_context import LdContext
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RetrieveTypeInfo200Response(BaseModel):
    """
    RetrieveTypeInfo200Response
    """
    id: StrictStr = Field(description="Fully Qualified Name (FQN) of the entity type being described. ")
    type: StrictStr = Field(description="JSON-LD @type. ")
    type_name: StrictStr = Field(description="Name of the entity type, short name if contained in @context. ", alias="typeName")
    entity_count: Union[StrictFloat, StrictInt] = Field(description="Number of entity instances of this entity type. ", alias="entityCount")
    attribute_details: List[Attribute] = Field(description="List of attributes that entity instances with the specified entity type can have. ", alias="attributeDetails")
    context: LdContext = Field(alias="@context")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "typeName", "entityCount", "attributeDetails", "@context"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('EntityTypeInfo'):
            raise ValueError("must be one of enum values ('EntityTypeInfo')")
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
        """Create an instance of RetrieveTypeInfo200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_details (list)
        _items = []
        if self.attribute_details:
            for _item in self.attribute_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributeDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of RetrieveTypeInfo200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "typeName": obj.get("typeName"),
            "entityCount": obj.get("entityCount"),
            "attributeDetails": [Attribute.from_dict(_item) for _item in obj.get("attributeDetails")] if obj.get("attributeDetails") is not None else None,
            "@context": LdContext.from_dict(obj.get("@context")) if obj.get("@context") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


