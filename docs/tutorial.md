# Build a filesystem configuration model

We will validate a filesystem URL in a Pydantic model, write a file through that
filesystem, and serialize the model.

## Install

Use Python 3.10 or newer with Pydantic 2:

```console
python -m pip install fsspec-pydantic 'pydantic>=2'
```

## Define a model

Create `config_demo.py`:

```python
from pydantic import BaseModel

from fsspec_pydantic import FileSystem, Path


class Storage(BaseModel):
    fs: FileSystem


storage = Storage(fs="memory://")
storage.fs.pipe_file("/config-demo/message.txt", b"hello")
print(storage.fs.cat_file("/config-demo/message.txt"))
```

Run `python config_demo.py`:

```text
b'hello'
```

## Keep the filesystem with a path

Append:

```python
path = Path("memory:///config-demo/message.txt")
print(path.isfile())
print(str(path))
```

Run the script again. The new lines are:

```text
True
memory:///config-demo/message.txt
```

## Serialize the configuration

Append:

```python
print(storage.model_dump())
```

The final line contains a filesystem URL:

```text
{'fs': 'memory://'}
```

The model holds a filesystem object while its serialized form holds a string.
See [How to validate existing files and directories](how-to-validate.md) for path
fields with existence checks.
