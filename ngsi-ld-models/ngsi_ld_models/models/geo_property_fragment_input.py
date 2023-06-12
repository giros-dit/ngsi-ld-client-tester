# coding: utf-8

"""
    NGSI-LD metamodel and Sensor NGSI-LD custom model

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API; NGSI-LD metamodel and Sensor NGSI-LD custom model.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from ngsi_ld_models.models.geometry import Geometry

class GeoPropertyFragmentInput(BaseModel):
    """
    GeoPropertyFragmentInput
    """
    type: Optional[StrictStr] = Field(None, description="Node type. ")
    value: Optional[Geometry] = None
    observed_at: Optional[datetime] = Field(None, alias="observedAt", description="Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ")
    dataset_id: Optional[StrictStr] = Field(None, alias="datasetId", description="It allows identifying a set or group of property values. ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["type", "value", "observedAt", "datasetId"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('GeoProperty'):
            raise ValueError("must be one of enum values ('GeoProperty')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GeoPropertyFragmentInput:
        """Create an instance of GeoPropertyFragmentInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeoPropertyFragmentInput:
        """Create an instance of GeoPropertyFragmentInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GeoPropertyFragmentInput.parse_obj(obj)

        _obj = GeoPropertyFragmentInput.parse_obj({
            "type": obj.get("type"),
            "value": Geometry.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "observed_at": obj.get("observedAt"),
            "dataset_id": obj.get("datasetId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

