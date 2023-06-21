# CreateSourceResponse


## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                        | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `status_code`                                                                                         | *int*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `raw_response`                                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                 | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `create_source_200_application_json_object`                                                           | [Optional[CreateSource200ApplicationJSON]](../../models/operations/createsource200applicationjson.md) | :heavy_minus_sign:                                                                                    | Successfully created source                                                                           |