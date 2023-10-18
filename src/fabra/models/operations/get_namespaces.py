"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import namespaces as shared_namespaces
from typing import Optional


@dataclasses.dataclass
class GetNamespacesRequest:
    connection_id: int = dataclasses.field(metadata={'query_param': { 'field_name': 'connectionID', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetNamespacesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    namespaces: Optional[shared_namespaces.Namespaces] = dataclasses.field(default=None)
    r"""Successfully fetched namespaces"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

