"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fabra import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class QueryFilter:
    field_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_name') }})
    field_value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_value') }})
    

