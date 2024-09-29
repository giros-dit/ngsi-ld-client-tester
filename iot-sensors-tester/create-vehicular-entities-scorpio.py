import logging
import logging.config
import yaml
import os
import ngsi_ld_client

# Importing Python library modules to use the OpenAPI schemas defined for the IoT use case:
from ngsi_ld_models.models.vehicle import Vehicle
from ngsi_ld_models.models.off_street_parking import OffStreetParking
from ngsi_ld_models.models.available_spot_number import AvailableSpotNumber
from ngsi_ld_models.models.person import Person
from ngsi_ld_models.models.camera import Camera
from ngsi_ld_models.models.company import Company
from ngsi_ld_models.models.city import City
from ngsi_ld_models.models.is_parked import IsParked
from ngsi_ld_models.models.passengers import Passengers
from ngsi_ld_models.models.route import Route
from ngsi_ld_models.models.provided_by import ProvidedBy
from ngsi_ld_models.models.operated_by import OperatedBy

# Importing Python library modules to use the self-defined OpenAPI schemas within the NGSI-LD OAS:
from ngsi_ld_client.models.entity import Entity
from ngsi_ld_models.models.geo_property import GeoProperty
from ngsi_ld_models.models.geometry_point import GeometryPoint
from ngsi_ld_models.models.geometry import Geometry
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

# Importing Python library modules to use the NGSI-LD API client:
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException

import time
import numpy as np

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

current_time = time.time_ns()
logger.info(f"Current time in nanoseconds in epoch time format: {current_time}") 
datetime_ns = np.datetime64(current_time, 'ns')
logger.info(f"Current date time in nanoseconds: {datetime_ns}")
observed_at = str(datetime_ns.astype('datetime64[ms]')) + 'Z'
logger.info(f"Current data time in nanoseconds in Zulu format: {observed_at}")

parking_company = Company(
    id="urn:ngsi-ld:Company:BigParkingCorp",
    type="Company",
    name={"type":"Property", "value": "BigParkingCorp"}
)

entity_input = parking_company.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type Company: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

parking_camera = Camera(
    id="urn:ngsi-ld:Camera:C1",
    type="Camera",
    name={"type":"Property", "value": "C1"}
)

entity_input = parking_camera.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type Camera: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

availableSpotNumber=AvailableSpotNumber(
    observed_at=observed_at,
    value=121,
    reliability={"type":"Property", "value":0.7},
    providedBy=ProvidedBy.from_dict({"type": "Relationship", "object": "urn:ngsi-ld:Camera:C1"})
)

parking_location = GeometryPoint(
    type="Point",
    coordinates=[-8.5, 41.2]
)

parking_location=Geometry.from_dict(parking_location.to_dict())

geoproperty_location = GeoProperty(
    type="GeoProperty",
    value=parking_location
)

parking=OffStreetParking(
    id="urn:ngsi-ld:OffStreetParking:Downtown1",
    type="OffStreetParking",
    location=GeoProperty.from_dict({"type":"GeoProperty", "value":parking_location.to_dict()}), #geoproperty_location.to_dict(),
    name={"type":"Property", "value":"Top Parking"},
    operatedBy=OperatedBy.from_dict({"type":"Relationship", "object": "urn:ngsi-ld:Company:BigParkingCorp"}),
    availableSpotNumber=availableSpotNumber,
    totalSpotNumber={"type":"Property", "value": 200}
)

entity_input = parking.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type OffStreetParking: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

person_bob=Person(
    id="urn:ngsi-ld:Person:Bob",
    type="Person",
    name={"type":"Property", "value": "Bob"}
)

entity_input = person_bob.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type Person: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

person_alice=Person(
    id="urn:ngsi-ld:Person:Bob",
    type="Person",
    name={"type":"Property", "value": "Alice"}
)

entity_input = person_alice.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type Person: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

city_antwerp=City(
    id="urn:ngsi-ld:City:Antwerp",
    type="City",
    name={"type":"Property", "value": "Antwerp"}
)

entity_input = city_antwerp.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type City: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

city_rotterdam=City(
    id="urn:ngsi-ld:City:Rotterdam",
    type="City",
    name={"type":"Property", "value": "Rotterdam"}
)

entity_input = city_rotterdam.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type City: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

city_amsterdam=City(
    id="urn:ngsi-ld:City:Amsterdam",
    type="City",
    name={"type":"Property", "value": "Amsterdam"}
)

entity_input = city_amsterdam.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type City: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

isParked = IsParked(
    type="Relationship",
    object="urn:ngsi-ld:OffStreetParking:Downtown1",
    objectType="OffStreetParking",
    observedAt=observed_at,
    providedBy=ProvidedBy.from_dict({"type": "Relationship", "object": "urn:ngsi-ld:Person:Bob"}),
)

passengers = Passengers(
    type="Relationship",
    object=["urn:ngsi-ld:Person:Alice", "urn:ngsi-ld:Person:Bob"],
    objectType="Person"
)

route = Route(
    type="ListRelationship",
    objectList=[{"object": "urn:ngsi-ld:City:Antwerp"}, {"object": "urn:ngsi-ld:City:Rotterdam"}, {"object": "urn:ngsi-ld:City:Amsterdam"}],
    objectType="City"
)

vehicle = Vehicle(
    id="urn:ngsi-ld:Vehicle:A4567",
    type="Vehicle",
    brandName={"type":"Property", "value":"Mercedes"},
    street={"type":"LanguageProperty", "languageMap": {"fr": "Grand Place", "nl": "Grote Markt"}},
    isParked=isParked,
    category={"type":"VocabProperty", "vocab": "non-commercial"},
    tyreTreadDepths={"type":"ListProperty", "valueList": ["300", "300", "120", "6"], "unitCode": "MMT"},
    passengers=passengers,
    route=route
)

entity_input = vehicle.to_dict()

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type Vehicle: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)