"""
Base Package

This package provides the fundamental modules for
the storage and management of objects.

Modules:
- file_storage: Handles the serialization and
deserialization of objects to/from JSON files.

Variables:
- storage: An instance of the FileStorage class for object storage.
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
