# Entity

5.2.4 NGSI-LD Entity. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | [**EntityType**](EntityType.md) |  | [optional] 
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) | Default geospatial Property of an entity. See clause 4.7.  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) | See clause 4.7.  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.entity import Entity

# TODO update the JSON string below
json = "{}"
# create an instance of Entity from a JSON string
entity_instance = Entity.from_json(json)
# print the JSON string representation of the object
print(Entity.to_json())

# convert the object into a dict
entity_dict = entity_instance.to_dict()
# create an instance of Entity from a dict
entity_from_dict = Entity.from_dict(entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


