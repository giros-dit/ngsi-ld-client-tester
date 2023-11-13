import logging
import os
from time import sleep
from fastapi import FastAPI, Request, status
import json
import ngsi_ld_client
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration

logger = logging.getLogger(__name__)

# NGSI-LD Context Broker
BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")
#BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")
# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

# Notifier
NOTIFIER_URI = os.getenv("NOTIFIER_URI", "http://notifier-consumer:8082/notify")

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

LIST_ENTITIES = [
    "IotDevice"
]

# Init FastAPI server
app = FastAPI(
    title="Notifier Tester API",
    version="1.0.0")

@app.on_event("startup")
async def startup_event():

    for entity in LIST_ENTITIES:
        endpoint = Endpoint(
            uri = NOTIFIER_URI,
            accept="application/json"
        )

        # Periodic Subscriptions
        """
        notification_params = NotificationParams (
            endpoint=endpoint,
            format="normalized"
            # attributes=["name"]
        )

        subs_request = CreateSubscriptionRequest (
            id="urn:ngsi-ld:Subscription:Periodic:{0}".format(entity),
            type="Subscription",
            entities=[{ "type": entity }],
            description="Periodic subscription to entities.",
            timeInterval= 10,
            notification=notification_params
        )
        """

        # On-Change Subscriptions
        notification_params = NotificationParams (
            endpoint=endpoint,
            format="normalized",
            attributes=["name", "hasSensor"],
            # sysAttrs=True,
            # showChanges=True
        )

        subs_request = CreateSubscriptionRequest (
            id="urn:ngsi-ld:Subscription:OnChange:{0}".format(entity),
            type="Subscription",
            entities=[{ "type": entity }],
            description="On-change subscription to entities for changes within the property name.",
            watchedAttributes=["name", "hasSensor"],
            notification=notification_params
        )

        api_instance = ngsi_ld_client.ContextInformationSubscriptionApi(ngsi_ld)
        api_instance.create_subscription(create_subscription_request=subs_request)

@app.post("/notify",
          status_code=status.HTTP_200_OK)
async def receiveNotification(request: Request):
    notification = await request.json()
    for entity in notification["data"]:
        logger.info("Entity notification: %s\n" % entity)