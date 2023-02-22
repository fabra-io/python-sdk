# fabra

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install fabra
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import fabra
from fabra.models import operations, shared

s = fabra.Fabra()
s.config_security(
    security=shared.Security(
        api_key_auth=shared.SchemeAPIKeyAuth(
            api_key="YOUR_API_KEY_HERE",
        ),
    )
)
   
req = operations.GetNamespacesRequest(
    query_params=operations.GetNamespacesQueryParams(
        connection_id=548814,
    ),
)
    
res = s.connection.get_namespaces(req)

if res.get_namespaces_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### connection

* `get_namespaces` - Get all namespaces
* `get_schema` - Get schema for table
* `get_tables` - Get all tables

### destination

* `create_destination` - Create a new destination
* `get_destinations` - Get all destinations

### object

* `create_object` - Create a new object
* `get_objects` - Get all objects

### source

* `create_source` - Create a new source
* `get_sources` - Get all sources

### sync

* `create_sync` - Create a new sync
* `get_syncs` - Get all syncs
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
