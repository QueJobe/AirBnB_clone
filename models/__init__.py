#!/usr/bin/python3
""" 
module that runs whenever the import of a model package occurs.
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
