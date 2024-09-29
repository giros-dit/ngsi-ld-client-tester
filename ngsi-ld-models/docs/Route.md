# Route

NGSI-LD ListRelationship type to identify the route of the vehicle (i.e., the list of identifier of NGSI-LD Entities of type City). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'ListRelationship']
**object_list** | **List[object]** |  | 
**object_type** | **str** |  | [optional] 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a ListRelationship instance as mandated by clause 4.5.8. System generated. Only used in temporal representation of ListRelationships.  | [optional] [readonly] 
**previous_object_list** | [**ListRelationshipPreviousObjectList**](ListRelationshipPreviousObjectList.md) |  | [optional] 
**entity_list** | [**List[Entity]**](Entity.md) | An array of inline Entity obtained by Linked Entity Retrieval, corresponding  to the ListRelationship&#39;s target object. See clause 4.5.23.2. Only used in  Linked Entity Retrieval, if the join&#x3D;inline option is explicitly requested.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_models.models.route import Route

# TODO update the JSON string below
json = "{}"
# create an instance of Route from a JSON string
route_instance = Route.from_json(json)
# print the JSON string representation of the object
print(Route.to_json())

# convert the object into a dict
route_dict = route_instance.to_dict()
# create an instance of Route from a dict
route_from_dict = Route.from_dict(route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


