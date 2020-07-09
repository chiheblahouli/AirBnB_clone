#!/usr/bin/python3
'''initializes repo as a module, includes file storage'''
from models.engine import file_storage


__all__ = ["base_model", "amenity", "city", "user", "state", "place", "review"]
storage = file_storage.FileStorage()
storage.reload()
