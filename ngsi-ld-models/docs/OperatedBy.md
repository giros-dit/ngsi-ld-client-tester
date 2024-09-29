# OperatedBy

NGSI-LD Relationship type to identify the company that operates the parking (i.e., the identifier of an NGSI-LD Entity of type Company). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Relationship']
**object** | **str** |  | 
**object_type** | [**RelationshipObjectType**](RelationshipObjectType.md) |  | [optional] 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Relationship instance as mandated by clause 4.5.8. System generated. Only used in temporal representation of Relationships.  | [optional] [readonly] 
**previous_object** | [**RelationshipPreviousObject**](RelationshipPreviousObject.md) |  | [optional] 
**entity** | [**RelationshipEntity**](RelationshipEntity.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.operated_by import OperatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of OperatedBy from a JSON string
operated_by_instance = OperatedBy.from_json(json)
# print the JSON string representation of the object
print(OperatedBy.to_json())

# convert the object into a dict
operated_by_dict = operated_by_instance.to_dict()
# create an instance of OperatedBy from a dict
operated_by_from_dict = OperatedBy.from_dict(operated_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


