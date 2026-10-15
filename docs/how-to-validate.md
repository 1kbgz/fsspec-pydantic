# How to validate existing files and directories

Use `FilePath` and `DirectoryPath` model fields to require that a path exists
and has the expected kind.

```python
import fsspec
from pydantic import BaseModel, ValidationError

from fsspec_pydantic import DirectoryPath, FilePath


class Input(BaseModel):
    source: FilePath
    directory: DirectoryPath


fs = fsspec.filesystem("memory")
fs.makedirs("/validation-demo", exist_ok=True)
fs.pipe_file("/validation-demo/input.csv", b"id\n1\n")

config = Input(
    source="memory:///validation-demo/input.csv",
    directory="memory:///validation-demo",
)
print(config.model_dump())

try:
    Input(source="memory:///validation-demo/missing.csv", directory=config.directory)
except ValidationError as error:
    print(error.errors()[0]["msg"])
```

The invalid input reports `Value error, Not a file`. Install the backend package
required by a remote URL and configure its credentials before validating.
Validation calls `isfile` or `isdir` and can perform remote I/O.

Pass an existing `Path` only when its stored kind is already trustworthy; validation
of a `Path` checks its stored `type` rather than querying the backend again.
