# coding: utf-8

"""
    Example schemas for IoT device with temperature and humidity sensors and for vehicles.

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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ngsi_ld_models.models.entity_scope import EntityScope
from ngsi_ld_models.models.geo_property import GeoProperty
from ngsi_ld_models.models.has_humidity_sensor import HasHumiditySensor
from ngsi_ld_models.models.has_temperature_sensor import HasTemperatureSensor
from ngsi_ld_models.models.iot_description import IotDescription
from ngsi_ld_models.models.iot_name import IotName
from typing import Optional, Set
from typing_extensions import Self

class IotDevice(BaseModel):
    """
    NGSI-LD Entity Type that represents an IoT device. 
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Entity id. ")
    type: StrictStr = Field(description="NGSI-LD Entity identifier. It has to be IotDevice.")
    scope: Optional[EntityScope] = None
    location: Optional[GeoProperty] = None
    observation_space: Optional[GeoProperty] = Field(default=None, alias="observationSpace")
    operation_space: Optional[GeoProperty] = Field(default=None, alias="operationSpace")
    created_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    name: Optional[IotName] = None
    description: IotDescription
    has_temperature_sensor: Optional[HasTemperatureSensor] = Field(default=None, alias="hasTemperatureSensor")
    has_humidity_sensor: Optional[HasHumiditySensor] = Field(default=None, alias="hasHumiditySensor")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "scope", "location", "observationSpace", "operationSpace", "createdAt", "modifiedAt", "deletedAt", "name", "description", "hasTemperatureSensor", "hasHumiditySensor"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['IotDevice']):
            raise ValueError("must be one of enum values ('IotDevice')")
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
        """Create an instance of IotDevice from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of observation_space
        if self.observation_space:
            _dict['observationSpace'] = self.observation_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation_space
        if self.operation_space:
            _dict['operationSpace'] = self.operation_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of has_temperature_sensor
        if self.has_temperature_sensor:
            _dict['hasTemperatureSensor'] = self.has_temperature_sensor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of has_humidity_sensor
        if self.has_humidity_sensor:
            _dict['hasHumiditySensor'] = self.has_humidity_sensor.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IotDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type") if obj.get("type") is not None else 'IotDevice',
            "scope": EntityScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "location": GeoProperty.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "observationSpace": GeoProperty.from_dict(obj["observationSpace"]) if obj.get("observationSpace") is not None else None,
            "operationSpace": GeoProperty.from_dict(obj["operationSpace"]) if obj.get("operationSpace") is not None else None,
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "name": IotName.from_dict(obj["name"]) if obj.get("name") is not None else None,
            "description": IotDescription.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "hasTemperatureSensor": HasTemperatureSensor.from_dict(obj["hasTemperatureSensor"]) if obj.get("hasTemperatureSensor") is not None else None,
            "hasHumiditySensor": HasHumiditySensor.from_dict(obj["hasHumiditySensor"]) if obj.get("hasHumiditySensor") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


