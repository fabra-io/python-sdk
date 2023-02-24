from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fabra import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RedshiftConfig:
    database_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('database_name') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('host') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('password') }})
    port: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('port') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('username') }})
    