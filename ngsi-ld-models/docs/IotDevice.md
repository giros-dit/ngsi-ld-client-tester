# IotDevice

NGSI-LD Entity Type that represents an IoT device. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be IotDevice. | [default to 'IotDevice']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) | Default geospatial Property of an entity. See clause 4.7.  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**name** | [**IotName**](IotName.md) |  | [optional] 
**description** | [**IotDescription**](IotDescription.md) |  | 
**has_temperature_sensor** | [**HasTemperatureSensor**](HasTemperatureSensor.md) |  | [optional] 
**has_humidity_sensor** | [**HasHumiditySensor**](HasHumiditySensor.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.iot_device import IotDevice

# TODO update the JSON string below
json = "{}"
# create an instance of IotDevice from a JSON string
iot_device_instance = IotDevice.from_json(json)
# print the JSON string representation of the object
print(IotDevice.to_json())

# convert the object into a dict
iot_device_dict = iot_device_instance.to_dict()
# create an instance of IotDevice from a dict
iot_device_from_dict = IotDevice.from_dict(iot_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


