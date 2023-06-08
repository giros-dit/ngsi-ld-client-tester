import logging
import os
import json


import ngsi_ld_client
from ngsi_ld_client.models.sensor import Sensor

from ngsi_ld_client.models.entity_input import EntityInput
from ngsi_ld_client.models.property_input import PropertyInput
from ngsi_ld_client.models.relationship_input import RelationshipInput

from ngsi_ld_client.models.entity_fragment_input import EntityFragmentInput
from fastapi import FastAPI, Request, status
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)

# NGSI-LD Context Broker
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:1026/v2")
# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://localhost:8080/context/interface/context.jsonld")


# Init NGSI-LD Client
configuration = NGSILDConfiguration(host=BROKER_URI)
ngsi_ld = NGSILDClient(configuration=configuration)

ngsi_ld.set_default_header(
    header_name="Link",
    header_value='<{0}>; '
                 'rel="http://www.w3.org/ns/json-ld#context"; '
                 'type="application/ld+json"'.format(CONTEXT_CATALOG_URI)
)

ngsi_ld.set_default_header(
    header_name="Accept",
    header_value="application/json"
)

sensor = Sensor(
    id="urn:ngsi-ld:Sensor:3",
    type="Sensor",
    name=PropertyInput(type="Property", value="iot-sensor"),
    description=PropertyInput(type="Property", value="IoT sensor"),
    temperature=PropertyInput(type="Property", value=10),
    humidity=PropertyInput(type="Property", value=20)
)

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

entity_input = sensor.dict(exclude_defaults=False, exclude_none=True, by_alias=False)
#entity_input = sensor.json(exclude_defaults=False, exclude_none=True, by_alias=False)

logger.info(entity_input)

print(EntityInput.from_dict(entity_input))

try:
    # Entity creation 
    api_instance.create_entity(entity_input=entity_input)
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

