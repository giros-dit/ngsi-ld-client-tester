# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from ngsi_ld_models.models.entity import Entity
from ngsi_ld_models.models.feature_collection import FeatureCollection
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

NOTIFICATIONDATA_ONE_OF_SCHEMAS = ["FeatureCollection", "List[Entity]"]

class NotificationData(BaseModel):
    """
    The content of the notification as NGSI-LD Entities. See clause 5.2.4.  If the notification has been triggered from a Subscription that has the notification. endpoint.accept field set to application/geo+json then data is returned as a FeatureCollection. In this case, if the notification.endpoint.rece iverInfo contains the key \"Prefer\" and it is set to the value \"body=json\", then the FeatureCollection will not contain an @context field.  If endpoint.accept is not set or holds another value then Entity[] is returned. 
    """
    # data type: List[Entity]
    oneof_schema_1_validator: Optional[List[Entity]] = None
    # data type: FeatureCollection
    oneof_schema_2_validator: Optional[FeatureCollection] = None
    actual_instance: Optional[Union[FeatureCollection, List[Entity]]] = None
    one_of_schemas: List[str] = Literal["FeatureCollection", "List[Entity]"]

    model_config = {
        "validate_assignment": True
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = NotificationData.model_construct()
        error_messages = []
        match = 0
        # validate data type: List[Entity]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: FeatureCollection
        if not isinstance(v, FeatureCollection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FeatureCollection`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in NotificationData with oneOf schemas: FeatureCollection, List[Entity]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in NotificationData with oneOf schemas: FeatureCollection, List[Entity]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into List[Entity]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FeatureCollection
        try:
            instance.actual_instance = FeatureCollection.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into NotificationData with oneOf schemas: FeatureCollection, List[Entity]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into NotificationData with oneOf schemas: FeatureCollection, List[Entity]. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


