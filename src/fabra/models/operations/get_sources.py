"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import source as shared_source
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSourcesResponseBody:
    r"""Successfully fetched sources"""
    sources: Optional[List[shared_source.Source]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sources'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetSourcesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[GetSourcesResponseBody] = dataclasses.field(default=None)
    r"""Successfully fetched sources"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

