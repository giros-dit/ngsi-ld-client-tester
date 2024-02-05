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

from datetime import datetime
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ngsi_ld_models.models.geometry import Geometry
from ngsi_ld_models.models.ld_context import LdContext
from ngsi_ld_models.models.property_previous_value import PropertyPreviousValue
from typing import Optional, Set
from typing_extensions import Self

class ReplaceAttrsRequest1(BaseModel):
    """
    ReplaceAttrsRequest1
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default='LanguageProperty', description="Node type. ")
    value: Optional[Geometry] = None
    observed_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ", alias="observedAt")
    unit_code: Optional[StrictStr] = Field(default=None, description="Property Value's unit code. ", alias="unitCode")
    dataset_id: Optional[StrictStr] = Field(default=None, description="It allows identifying a set or group of property values. ", alias="datasetId")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    instance_id: Optional[StrictStr] = Field(default=None, description="A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated. ", alias="instanceId")
    previous_value: Optional[PropertyPreviousValue] = Field(default=None, alias="previousValue")
    object: Optional[StrictStr] = Field(default=None, description="Relationship's target object. ")
    previous_object: Optional[StrictStr] = Field(default=None, description="Previous Relationship's target object. Only used in notifications. ", alias="previousObject")
    language_map: Optional[Dict[str, Any]] = Field(default=None, description="String Property Values defined in multiple natural languages. ", alias="languageMap")
    previous_language_map: Optional[Dict[str, Any]] = Field(default=None, description="Previous Language Property languageMap. Only used in notifications. ", alias="previousLanguageMap")
    context: LdContext = Field(alias="@context")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "value", "observedAt", "unitCode", "datasetId", "createdAt", "modifiedAt", "deletedAt", "instanceId", "previousValue", "object", "previousObject", "languageMap", "previousLanguageMap", "@context"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('LanguageProperty'):
            raise ValueError("must be one of enum values ('LanguageProperty')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReplaceAttrsRequest1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "modified_at",
            "deleted_at",
            "instance_id",
            "previous_object",
            "previous_language_map",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous_value
        if self.previous_value:
            _dict['previousValue'] = self.previous_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReplaceAttrsRequest1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'LanguageProperty',
            "value": Geometry.from_dict(obj["value"]) if obj.get("value") is not None else None,
            "observedAt": obj.get("observedAt"),
            "unitCode": obj.get("unitCode"),
            "datasetId": obj.get("datasetId"),
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "instanceId": obj.get("instanceId"),
            "previousValue": PropertyPreviousValue.from_dict(obj["previousValue"]) if obj.get("previousValue") is not None else None,
            "object": obj.get("object"),
            "previousObject": obj.get("previousObject"),
            "languageMap": obj.get("languageMap"),
            "previousLanguageMap": obj.get("previousLanguageMap"),
            "@context": LdContext.from_dict(obj["@context"]) if obj.get("@context") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


