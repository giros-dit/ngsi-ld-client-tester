# TemperatureCoordinates

NGSI-LD Property Type. The temperature coordinates. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** | A single position.  | [optional] 
**temperature_coordinates_description** | [**TemperatureCoordinatesDescription**](TemperatureCoordinatesDescription.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.temperature_coordinates import TemperatureCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of TemperatureCoordinates from a JSON string
temperature_coordinates_instance = TemperatureCoordinates.from_json(json)
# print the JSON string representation of the object
print(TemperatureCoordinates.to_json())

# convert the object into a dict
temperature_coordinates_dict = temperature_coordinates_instance.to_dict()
# create an instance of TemperatureCoordinates from a dict
temperature_coordinates_from_dict = TemperatureCoordinates.from_dict(temperature_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


