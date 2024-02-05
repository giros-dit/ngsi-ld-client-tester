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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from ngsi_ld_models.models.key_value_pair import KeyValuePair
from typing import Optional, Set
from typing_extensions import Self

class Endpoint(BaseModel):
    """
    5.2.15 represents the parameters that are required in order to define an endpoint for notifications. 
    """ # noqa: E501
    uri: StrictStr = Field(description="URI which conveys the endpoint which will receive the notification. ")
    accept: Optional[StrictStr] = Field(default=None, description="Intended to convey the MIME type of the notification payload body (JSON, or JSON-LD, or GeoJSON). If not present, default is \"application/json\". ")
    timeout: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum period of time in milliseconds which may elapse before a notification is assumed to have failed. The NGSI-LD system can override this value. This only applies if the binding protocol always returns a response. ")
    cooldown: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Once a failure has occurred, minimum period of time in milliseconds which shall elapse before attempting to make a subsequent notification to the same endpoint after failure. If requests are received before the cooldown period has expired, no notification is sent. ")
    receiver_info: Optional[List[KeyValuePair]] = Field(default=None, description="Generic {key, value} array to convey optional information to the receiver. ", alias="receiverInfo")
    notifier_info: Optional[List[KeyValuePair]] = Field(default=None, description="Generic {key, value} array to set up the communication channel. ", alias="notifierInfo")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["uri", "accept", "timeout", "cooldown", "receiverInfo", "notifierInfo"]

    @field_validator('accept')
    def accept_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('application/json', 'application/ld+json', 'application/geo+json'):
            raise ValueError("must be one of enum values ('application/json', 'application/ld+json', 'application/geo+json')")
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
        """Create an instance of Endpoint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in receiver_info (list)
        _items = []
        if self.receiver_info:
            for _item in self.receiver_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['receiverInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notifier_info (list)
        _items = []
        if self.notifier_info:
            for _item in self.notifier_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notifierInfo'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Endpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "accept": obj.get("accept"),
            "timeout": obj.get("timeout"),
            "cooldown": obj.get("cooldown"),
            "receiverInfo": [KeyValuePair.from_dict(_item) for _item in obj["receiverInfo"]] if obj.get("receiverInfo") is not None else None,
            "notifierInfo": [KeyValuePair.from_dict(_item) for _item in obj["notifierInfo"]] if obj.get("notifierInfo") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


