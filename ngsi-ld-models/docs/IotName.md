# IotName

NGSI-LD Property Type. The IoT device name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | 
**observed_at** | **datetime** | Timestamp. See clause 4.8.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.iot_name import IotName

# TODO update the JSON string below
json = "{}"
# create an instance of IotName from a JSON string
iot_name_instance = IotName.from_json(json)
# print the JSON string representation of the object
print(IotName.to_json())

# convert the object into a dict
iot_name_dict = iot_name_instance.to_dict()
# create an instance of IotName from a dict
iot_name_from_dict = IotName.from_dict(iot_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


