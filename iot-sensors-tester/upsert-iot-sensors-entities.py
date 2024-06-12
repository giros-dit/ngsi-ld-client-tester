import logging
import logging.config
import yaml
import os

import ngsi_ld_client
from ngsi_ld_models.models.iot_device import IotDevice
from ngsi_ld_models.models.temperature_sensor import TemperatureSensor
from ngsi_ld_models.models.humidity_sensor import HumiditySensor
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

entities_input = []

iot_device = IotDevice(
    id="urn:ngsi-ld:IotDevice:1",
    type="IotDevice",
    name={"type":"Property", "value": "IoTDevice"},
    description={"type": "Property", "value": "IoT device with sensors."},
    hasTemperatureSensor={"type": "Relationship", "object": "urn:ngsi-ld:TemperatureSensor:1"},
    hasHumiditySensor={"type": "Relationship", "object": "urn:ngsi-ld:HumiditySensor:1"}
)

temperature_sensor = TemperatureSensor(
    id="urn:ngsi-ld:TemperatureSensor:1",
    type="TemperatureSensor",
    temperature={"type":"Property", "value": 29.9, "unitCode": "CEL"}
)

humidity_sensor = HumiditySensor(
    id="urn:ngsi-ld:HumiditySensor:1",
    type="HumiditySensor",
    humidity={"type":"Property", "value": 32.8, "unitCode": "P1"}
)

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

iot_device_entity_input = iot_device.to_dict()

logger.info("IotDevice object representation: %s\n" % iot_device)

logger.info("Entity object representation for IotDevice object: %s\n" % Entity.from_dict(iot_device_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(iot_device_entity_input))

temperature_sensor_entity_input = temperature_sensor.to_dict()

logger.info("TemperatureSensor object representation: %s\n" % temperature_sensor_entity_input)

logger.info("Entity object representation for TemperatureSensor object: %s\n" % Entity.from_dict(temperature_sensor_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(temperature_sensor_entity_input))

humidity_sensor_entity_input = humidity_sensor.to_dict()

logger.info("HumiditySensorobject representation: %s\n" % humidity_sensor_entity_input)

logger.info("Entity object representation for HumiditySensor object: %s\n" % Entity.from_dict(humidity_sensor_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(humidity_sensor_entity_input))

try:
    # Create NGSI-LD entities of type Interface and Sensor: POST /entityOperations/upsert
    api_instance.upsert_batch(query_entity200_response_inner=entities_input)
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->upsert_batch: %s\n" % e)

