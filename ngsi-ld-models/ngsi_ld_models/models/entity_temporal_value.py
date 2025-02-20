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
import pprint
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ngsi_ld_models.models.geo_property import GeoProperty
from ngsi_ld_models.models.language_property import LanguageProperty
from ngsi_ld_models.models.model_property import ModelProperty
from ngsi_ld_models.models.relationship import Relationship
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

ENTITYTEMPORALVALUE_ONE_OF_SCHEMAS = ["List[GeoProperty]", "List[LanguageProperty]", "List[ModelProperty]", "List[Relationship]"]

class EntityTemporalValue(BaseModel):
    """
    EntityTemporalValue
    """
    # data type: List[ModelProperty]
    oneof_schema_1_validator: Optional[List[ModelProperty]] = None
    # data type: List[Relationship]
    oneof_schema_2_validator: Optional[List[Relationship]] = None
    # data type: List[GeoProperty]
    oneof_schema_3_validator: Optional[List[GeoProperty]] = None
    # data type: List[LanguageProperty]
    oneof_schema_4_validator: Optional[List[LanguageProperty]] = None
    actual_instance: Optional[Union[List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship]]] = None
    one_of_schemas: List[str] = Field(default=Literal["List[GeoProperty]", "List[LanguageProperty]", "List[ModelProperty]", "List[Relationship]"])

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
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
        instance = EntityTemporalValue.model_construct()
        error_messages = []
        match = 0
        # validate data type: List[ModelProperty]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[Relationship]
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[GeoProperty]
        try:
            instance.oneof_schema_3_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[LanguageProperty]
        try:
            instance.oneof_schema_4_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EntityTemporalValue with oneOf schemas: List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EntityTemporalValue with oneOf schemas: List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into List[ModelProperty]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[Relationship]
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[GeoProperty]
        try:
            # validation
            instance.oneof_schema_3_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_3_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[LanguageProperty]
        try:
            # validation
            instance.oneof_schema_4_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_4_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EntityTemporalValue with oneOf schemas: List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EntityTemporalValue with oneOf schemas: List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship]. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], List[GeoProperty], List[LanguageProperty], List[ModelProperty], List[Relationship]]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


