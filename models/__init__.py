"""
Create global variable storage whioch handles saving of instances
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
