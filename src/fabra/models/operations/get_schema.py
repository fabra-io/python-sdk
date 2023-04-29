"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import field as shared_field
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class GetSchemaRequest:
    
    connection_id: int = dataclasses.field(metadata={'query_param': { 'field_name': 'connectionID', 'style': 'form', 'explode': True }})
    namespace: str = dataclasses.field(metadata={'query_param': { 'field_name': 'namespace', 'style': 'form', 'explode': True }})
    table_name: str = dataclasses.field(metadata={'query_param': { 'field_name': 'tableName', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSchema200ApplicationJSON:
    r"""Successfully fetched schema"""
    
    schema: Optional[list[shared_field.Field]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSchemaResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_schema_200_application_json_object: Optional[GetSchema200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successfully fetched schema"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    