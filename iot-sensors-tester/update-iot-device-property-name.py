import logging
import logging.config
import os
import yaml

import ngsi_ld_client

from ngsi_ld_models.models.iot_device import IotDevice
from ngsi_ld_models.models.name import Name
from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.model_property import ModelProperty
from ngsi_ld_client.models.property_value import PropertyValue

from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException
from ngsi_ld_client.models.replace_attrs_request import ReplaceAttrsRequest

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



api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

'''
name = Name(
    type='Property',
    value='IotDeviceSensors'
)

property_input = name.to_dict()
logger.info("Name object representation: %s\n" % property_input)
property_value = PropertyValue.from_dict(property_input)
'''

property_value=PropertyValue('IotDeviceSensors')
logger.info("PropertyValue object representation: %s\n" % property_value)

model_property = ModelProperty(value=property_value)

rap = ReplaceAttrsRequest(model_property)
       
try:
    # Partial Attribute update by Attribute id: PATCH /entities/{entityId}/attrs/{attrId}
    api_instance.update_attrs(entity_id='urn:ngsi-ld:IotDevice:1', attr_id='name', replace_attrs_request=rap)
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->update_attrs: %s\n" % e)

