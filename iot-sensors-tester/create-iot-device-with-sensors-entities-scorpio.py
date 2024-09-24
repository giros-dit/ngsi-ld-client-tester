import logging
import logging.config
import yaml
import os
import ngsi_ld_client

# Importing Python library modules to use the OpenAPI schemas defined for the IoT use case:
from ngsi_ld_models.models.temperature_sensor import TemperatureSensor
from ngsi_ld_models.models.temperature import Temperature
from ngsi_ld_models.models.temperature_description import TemperatureDescription
from ngsi_ld_models.models.temperature_coordinates import TemperatureCoordinates
from ngsi_ld_models.models.temperature_coordinates_description import TemperatureCoordinatesDescription
from ngsi_ld_models.models.humidity_sensor import HumiditySensor
from ngsi_ld_models.models.iot_device import IotDevice
from ngsi_ld_models.models.has_temperature_sensor import HasTemperatureSensor
from ngsi_ld_models.models.has_humidity_sensor import HasHumiditySensor
# Importing Python library modules to use the self-defined OpenAPI schemas within the NGSI-LD OAS:
from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.geometry import Geometry
from ngsi_ld_client.models.geometry_point import GeometryPoint
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

# Importing Python library modules to use the NGSI-LD API client:
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

# Context catalog service
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")

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

# Declaring API for Context Information Provision operations:
api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

temperature_sensor = TemperatureSensor(
    id="urn:ngsi-ld:TemperatureSensor:1",
    type="TemperatureSensor",
    temperature={"type":"Property", "value": 27.9, "unitCode": "CEL"}
)

entity_input = temperature_sensor.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type TemperatureSensor: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

humidity_sensor = HumiditySensor(
    id="urn:ngsi-ld:HumiditySensor:1",
    type="HumiditySensor",
    humidity={"type":"Property", "value": 30.8, "unitCode": "P1"}
)

entity_input = humidity_sensor.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type HumiditySensor: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

iot_device = IotDevice(
    id="urn:ngsi-ld:IotDevice:1",
    type="IotDevice",
    name={"type":"Property", "value": "IotSensors"},
    description={"type":"Property", "value": "IoT device with sensors."},
    hasTemperatureSensor=HasTemperatureSensor.from_dict({"type": "Relationship", "object": "urn:ngsi-ld:TemperatureSensor:1"}),
    hasHumiditySensor=HasHumiditySensor.from_dict({"type": "Relationship", "object": "urn:ngsi-ld:HumiditySensor:1"})
)

entity_input = iot_device.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type IotDevice: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)