"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import object as shared_object
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetObjects200ApplicationJSON:
    r"""Successfully fetched objects"""
    
    objects: Optional[list[shared_object.Object]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('objects'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class GetObjectsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    get_objects_200_application_json_object: Optional[GetObjects200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successfully fetched objects"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    