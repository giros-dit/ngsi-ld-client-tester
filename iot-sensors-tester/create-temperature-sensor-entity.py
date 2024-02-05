import logging
import logging.config
import yaml
import os

import ngsi_ld_client

from ngsi_ld_models.models.temperature_sensor import TemperatureSensor
from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException

#assuming the log config file name is logging.yaml
with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

#read the file to logging config
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

# NGSI-LD Context Broker
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:9090/ngsi-ld/v1")
# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

# Init NGSI-LD Client
configuration = NGSILDConfiguration(host=BROKER_URI)
configuration.debug = True
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

temperature_sensor = TemperatureSensor(
    id="urn:ngsi-ld:TemperatureSensor:1",
    type="TemperatureSensor",
    temperature={"type":"Property", "value": 27.9, "unitCode": "CEL"}
)

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

entity_input = temperature_sensor.to_dict()

logger.info("TemperatureSensor object representation: %s\n" % entity_input)

logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))

logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type Sensor: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

