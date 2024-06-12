# coding: utf-8

"""
    Example schemas for IoT device with temperature and humidity sensors

    Example schemas compliant with the NGSI-LD OAS metamodel according to ETSI GS CIM 009. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional, Union
from ngsi_ld_models.models.property_previous_value import PropertyPreviousValue
from ngsi_ld_models.models.system_generated_attributes import SystemGeneratedAttributes
from typing import Optional, Set
from typing_extensions import Self

class Humidity(BaseModel):
    """
    NGSI-LD Property Type. The humidity measurement. 
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default='Property', description="Node type. ")
    value: Union[StrictFloat, StrictInt]
    observed_at: Optional[datetime] = Field(default=None, description="Timestamp. See clause 4.8. ", alias="observedAt")
    unit_code: Optional[StrictStr] = Field(default=None, description="Property Value's unit code. ", alias="unitCode")
    dataset_id: Optional[StrictStr] = Field(default=None, description="It allows identifying a set or group of property values. ", alias="datasetId")
    system_generated_attrs: Optional[SystemGeneratedAttributes] = Field(default=None, alias="systemGeneratedAttrs")
    instance_id: Optional[StrictStr] = Field(default=None, description="A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated. ", alias="instanceId")
    previous_value: Optional[PropertyPreviousValue] = Field(default=None, alias="previousValue")
    __properties: ClassVar[List[str]] = ["type", "value", "observedAt", "unitCode", "datasetId", "systemGeneratedAttrs", "instanceId", "previousValue"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Property']):
            raise ValueError("must be one of enum values ('Property')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Humidity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "instance_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of system_generated_attrs
        if self.system_generated_attrs:
            _dict['systemGeneratedAttrs'] = self.system_generated_attrs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous_value
        if self.previous_value:
            _dict['previousValue'] = self.previous_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Humidity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Humidity) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'Property',
            "value": obj.get("value"),
            "observedAt": obj.get("observedAt"),
            "unitCode": obj.get("unitCode"),
            "datasetId": obj.get("datasetId"),
            "systemGeneratedAttrs": SystemGeneratedAttributes.from_dict(obj["systemGeneratedAttrs"]) if obj.get("systemGeneratedAttrs") is not None else None,
            "instanceId": obj.get("instanceId"),
            "previousValue": PropertyPreviousValue.from_dict(obj["previousValue"]) if obj.get("previousValue") is not None else None
        })
        return _obj


