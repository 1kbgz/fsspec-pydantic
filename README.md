# fsspec-pydantic

Pydantic wrappers of fsspec types

[![Build Status](https://github.com/1kbgz/fsspec-pydantic/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/1kbgz/fsspec-pydantic/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/1kbgz/fsspec-pydantic/branch/main/graph/badge.svg)](https://codecov.io/gh/1kbgz/fsspec-pydantic)
[![License](https://img.shields.io/github/license/1kbgz/fsspec-pydantic)](https://github.com/1kbgz/fsspec-pydantic)
[![PyPI](https://img.shields.io/pypi/v/fsspec-pydantic.svg)](https://pypi.python.org/pypi/fsspec-pydantic)

## Overview

This library contains [Pydantic](https://github.com/pydantic/pydantic) validators for [fsspec](https://github.com/fsspec/filesystem_spec).

- `FileSystem = Annotated[AbstractFileSystem, FSSpecFilesystemType]`: Annotation for filesystem class
- `FilePath = Annotated[Path, FSSpecPathType(path_type="file")]`: Annotation for a file
- `DirectoryPath = Annotated[Path, FSSpecPathType(path_type="dir")]`: Annotation for a directory

This library can be used to include `fsspec` types in other Pydantic models.

> [!NOTE]
> This library was generated using [copier](https://copier.readthedocs.io/en/stable/) from the [Base Python Project Template repository](https://github.com/python-project-templates/base).
