# HumiditySensor

NGSI-LD Entity Type that represents a humidity sensor. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be HumiditySensor. | [default to 'HumiditySensor']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) | Default geospatial Property of an entity. See clause 4.7.  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**humidity** | [**Humidity**](Humidity.md) |  | 

## Example

```python
from ngsi_ld_models.models.humidity_sensor import HumiditySensor

# TODO update the JSON string below
json = "{}"
# create an instance of HumiditySensor from a JSON string
humidity_sensor_instance = HumiditySensor.from_json(json)
# print the JSON string representation of the object
print(HumiditySensor.to_json())

# convert the object into a dict
humidity_sensor_dict = humidity_sensor_instance.to_dict()
# create an instance of HumiditySensor from a dict
humidity_sensor_from_dict = HumiditySensor.from_dict(humidity_sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


