# Humidity

NGSI-LD Property Type. The humidity measurement. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **float** |  | 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.humidity import Humidity

# TODO update the JSON string below
json = "{}"
# create an instance of Humidity from a JSON string
humidity_instance = Humidity.from_json(json)
# print the JSON string representation of the object
print(Humidity.to_json())

# convert the object into a dict
humidity_dict = humidity_instance.to_dict()
# create an instance of Humidity from a dict
humidity_from_dict = Humidity.from_dict(humidity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


