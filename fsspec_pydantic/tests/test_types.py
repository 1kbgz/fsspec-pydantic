from pathlib import Path as BasePath

import pytest
from fsspec import AbstractFileSystem
from pydantic import TypeAdapter, ValidationError

from fsspec_pydantic import DirectoryPath, FilePath, FileSystem, Path


class TestFSSpecTypes:
    def test_fs(self):
        fs = FileSystem("local:///tmp")  # ty: ignore[call-non-callable]  # Annotated aliases forward calls to their underlying class.
        assert isinstance(fs, AbstractFileSystem)

    def test_file(self):
        file = FilePath("local:///tmp")  # ty: ignore[call-non-callable]  # Annotated aliases forward calls to their underlying class.
        print(type(file))
        assert isinstance(file, Path)
        assert isinstance(file.fs, AbstractFileSystem)
        assert isinstance(file.path, BasePath)
        assert str(file) == "file:///tmp"

    def test_dir(self):
        dir = DirectoryPath("local:///tmp")  # ty: ignore[call-non-callable]  # Annotated aliases forward calls to their underlying class.
        assert isinstance(dir, Path)
        assert isinstance(dir.fs, AbstractFileSystem)
        assert isinstance(dir.path, BasePath)
        assert str(dir) == "file:///tmp"

    def test_resolve(self):
        dir = Path("local:///tmp")
        assert dir.type == "fsspec-dir"
        file = Path(f"local://{__file__}")
        assert file.type == "fsspec-file"

    def test_path_validation(self, tmp_path):
        file = tmp_path / "data.txt"
        file.write_text("data")
        file_adapter = TypeAdapter(FilePath)
        dir_adapter = TypeAdapter(DirectoryPath)
        assert file_adapter.validate_python(str(file)).isfile()
        assert dir_adapter.validate_python(str(tmp_path)).isdir()
        with pytest.raises(ValidationError, match="Not a file"):
            file_adapter.validate_python(str(tmp_path))
        with pytest.raises(ValidationError, match="Not a dir"):
            dir_adapter.validate_python(str(file))
        assert file_adapter.json_schema()["format"] == "file-path"
        assert dir_adapter.json_schema()["format"] == "directory-path"

    def test_filesystem_serialization(self):
        adapter = TypeAdapter(FileSystem)
        fs = adapter.validate_python("memory://")
        assert isinstance(fs, AbstractFileSystem)
        assert adapter.dump_python(fs) == "memory://"

    def test_path_resolve(self, tmp_path):
        path = Path(str(tmp_path))
        resolved = path.resolve()
        assert resolved.isdir()
        assert resolved.path == tmp_path.resolve()
        assert hash(resolved) == hash(str(resolved))
