"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import queryfilter as shared_queryfilter
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QueryObjectRequestBody:
    filters: Optional[List[shared_queryfilter.QueryFilter]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class QueryObjectRequest:
    end_customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'endCustomerID', 'style': 'simple', 'explode': False }})
    object_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'objectID', 'style': 'simple', 'explode': False }})
    request_body: Optional[QueryObjectRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExampleField3:
    nested_field_1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nested_field_1'), 'exclude': lambda f: f is None }})
    nested_field_2: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nested_field_2'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QueryObjectResponseBody:
    r"""The response payload will match the schema you defined when creating the object"""
    example_field_1: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('example_field_1'), 'exclude': lambda f: f is None }})
    example_field_2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('example_field_2'), 'exclude': lambda f: f is None }})
    example_field_3: Optional[ExampleField3] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('example_field_3'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class QueryObjectResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[QueryObjectResponseBody] = dataclasses.field(default=None)
    r"""The response payload will match the schema you defined when creating the object"""
    

