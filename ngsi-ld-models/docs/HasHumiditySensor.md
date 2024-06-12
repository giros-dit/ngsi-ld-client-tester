# HasHumiditySensor

NGSI-LD Relationship Type to identify a humidity sensor of the IoT device (i.e., the identifier of an NGSI-LD     Entity of type HumiditySensor). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Relationship']
**object** | **str** |  | 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Relationship instance (see clause 4.5.8). System generated.  | [optional] [readonly] 
**previous_object** | **str** | Previous Relationship&#39;s target object. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_models.models.has_humidity_sensor import HasHumiditySensor

# TODO update the JSON string below
json = "{}"
# create an instance of HasHumiditySensor from a JSON string
has_humidity_sensor_instance = HasHumiditySensor.from_json(json)
# print the JSON string representation of the object
print(HasHumiditySensor.to_json())

# convert the object into a dict
has_humidity_sensor_dict = has_humidity_sensor_instance.to_dict()
# create an instance of HasHumiditySensor from a dict
has_humidity_sensor_from_dict = HasHumiditySensor.from_dict(has_humidity_sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


