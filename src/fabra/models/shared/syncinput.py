from __future__ import annotations
import dataclasses
from ..shared import fieldmapping as shared_fieldmapping
from ..shared import frequencyunits_enum as shared_frequencyunits_enum
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncInput:
    destination_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination_id') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name') }})
    field_mappings: list[shared_fieldmapping.FieldMapping] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_mappings') }})
    frequency: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency') }})
    frequency_units: shared_frequencyunits_enum.FrequencyUnitsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency_units') }})
    object_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_id') }})
    source_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_id') }})
    cursor_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor_field'), 'exclude': lambda f: f is None }})
    custom_join: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_join'), 'exclude': lambda f: f is None }})
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace'), 'exclude': lambda f: f is None }})
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_key'), 'exclude': lambda f: f is None }})
    table_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table_name'), 'exclude': lambda f: f is None }})
    