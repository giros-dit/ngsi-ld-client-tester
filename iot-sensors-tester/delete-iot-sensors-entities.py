import logging
import logging.config
import os
import yaml

import ngsi_ld_client
from ngsi_ld_models.models.iot_device import IotDevice
from ngsi_ld_models.models.temperature_sensor import TemperatureSensor
from ngsi_ld_models.models.humidity_sensor import HumiditySensor

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
                                "http://localhost:8080/context.jsonld")


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

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

try:
    # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
    api_instance.delete_entity(entity_id='urn:ngsi-ld:IotDevice:1')
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)

try:
    # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
    api_instance.delete_entity(entity_id='urn:ngsi-ld:TemperatureSensor:1')
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)

try:
    # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
    api_instance.delete_entity(entity_id='urn:ngsi-ld:HumiditySensor:1')
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)