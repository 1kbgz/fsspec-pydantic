# Type reference

The package exports `FileSystem`, `Path`, `FilePath`, and `DirectoryPath`.
Validator metadata classes are available from `fsspec_pydantic.types`.

## `FileSystem`

`Annotated[AbstractFileSystem, FSSpecFilesystemType]`. Accepts an existing fsspec
filesystem or resolves a URL through `get_fs_token_paths`. Serializes with
`fs.unstrip_protocol("")`. JSON Schema is a string with format `fsspec-fs`.

The serialized value identifies the filesystem protocol; it does not preserve
credentials, all storage options, or the root path of the input URL.

## `Path(fs, path=None, type=None)`

A dataclass containing `fs`, `path` (a `pathlib.Path`), and `type` (`fsspec-file` or
`fsspec-dir`). A string `fs` is resolved as a URL; an existing filesystem requires
`path`. With no explicit type, construction calls `isdir` to classify the path.
For a URL that is not a directory, construction classifies it as a file without
requiring it to exist.

| Member      | Result                                                                     |
| ----------- | -------------------------------------------------------------------------- |
| `isfile()`  | Whether stored `type` equals `fsspec-file`.                                |
| `isdir()`   | Whether stored `type` equals `fsspec-dir`.                                 |
| `str(path)` | URL from `fs.unstrip_protocol(path.path.as_posix())`.                      |
| `resolve()` | A new path using `pathlib.Path.resolve()` and backend directory detection. |

`resolve()` applies local pathlib resolution, including local working-directory
rules; it is not a backend-specific remote canonicalization operation.

## `FSSpecPathType(path_type)`

Pydantic 2 annotation metadata for `Path`.

| `path_type`   | String-input validation                                           | JSON Schema format |
| ------------- | ----------------------------------------------------------------- | ------------------ |
| `fsspec-file` | Requires `fs.isfile(path)`; otherwise `ValueError("Not a file")`. | `file-path`        |
| `fsspec-dir`  | Requires `fs.isdir(path)`; otherwise `ValueError("Not a dir")`.   | `directory-path`   |

Validated values serialize as URL strings. Existing `Path` inputs are checked by
stored `type`, without a fresh backend existence check.

## `FilePath` and `DirectoryPath`

`FilePath` is `Annotated[Path, FSSpecPathType(path_type="fsspec-file")]`.
`DirectoryPath` is `Annotated[Path, FSSpecPathType(path_type="fsspec-dir")]`.
Their validation and JSON Schema behavior follow the metadata above.

Constructing an alias directly, such as `FilePath(url)`, invokes `Path` construction
without Pydantic validation. Pydantic validation runs when the annotation is used
in a model field or a `TypeAdapter`.
