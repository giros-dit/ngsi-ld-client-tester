import logging
import logging.config
import os
from typing import List
import yaml

import ngsi_ld_client

from ngsi_ld_models.models.iot_device import IotDevice
from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.query_entity_options_parameter_inner import QueryEntityOptionsParameterInner
from ngsi_ld_client.models.options_sys_attrs import OptionsSysAttrs


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
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:1026/ngsi-ld/v1")
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

options = []

api_instance = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)

try:
    # Query NGSI-LD entities of type Sensor: GET /entities
    api_response = api_instance.query_entity(type='IotDevice')
    iot_device_entities = api_response
    for iot_device_entity in iot_device_entities:
        logger.info(iot_device_entity.to_dict())
except Exception as e:
    logger.exception("Exception when calling ContextInformationConsumptionApi->query_entity: %s\n" % e)
