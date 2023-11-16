"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import object as shared_object
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateObjectResponseBody:
    r"""Successfully created object"""
    object: Optional[shared_object.Object] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class CreateObjectResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[CreateObjectResponseBody] = dataclasses.field(default=None)
    r"""Successfully created object"""
    

