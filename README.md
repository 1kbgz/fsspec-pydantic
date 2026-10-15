# fsspec-pydantic

Represent fsspec filesystems and paths in Pydantic models.

[![Build Status](https://github.com/1kbgz/fsspec-pydantic/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/1kbgz/fsspec-pydantic/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/1kbgz/fsspec-pydantic/branch/main/graph/badge.svg)](https://codecov.io/gh/1kbgz/fsspec-pydantic)
[![License](https://img.shields.io/github/license/1kbgz/fsspec-pydantic)](https://github.com/1kbgz/fsspec-pydantic)
[![PyPI](https://img.shields.io/pypi/v/fsspec-pydantic.svg)](https://pypi.python.org/pypi/fsspec-pydantic)

`fsspec-pydantic` supplies a filesystem annotation and a path value that keeps its
filesystem alongside its backend path. Model serialization produces URL strings.

## Documentation

[Build a filesystem configuration model](docs/tutorial.md) walks through validation
and serialization. [Validate existing files and directories](docs/how-to-validate.md)
shows model fields with existence checks.

Consult the [type reference](docs/reference.md) for accepted inputs, serialization,
and the built-in path aliases. Read
[Why paths keep their filesystem](docs/explanation.md) for the model behind these types.
