# TemperatureSensor

NGSI-LD Entity Type that represents a temperature sensor. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be TemperatureSensor. | [default to 'TemperatureSensor']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) | Default geospatial Property of an entity. See clause 4.7.  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**temperature** | [**Temperature**](Temperature.md) |  | 

## Example

```python
from ngsi_ld_models.models.temperature_sensor import TemperatureSensor

# TODO update the JSON string below
json = "{}"
# create an instance of TemperatureSensor from a JSON string
temperature_sensor_instance = TemperatureSensor.from_json(json)
# print the JSON string representation of the object
print(TemperatureSensor.to_json())

# convert the object into a dict
temperature_sensor_dict = temperature_sensor_instance.to_dict()
# create an instance of TemperatureSensor from a dict
temperature_sensor_from_dict = TemperatureSensor.from_dict(temperature_sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


