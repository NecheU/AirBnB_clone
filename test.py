#!/usr/bin/python3
from models.engine.file_storage import FileStorage

fs = FileStorage()
print(fs)

try:
    print(type(FileStorage._FileStorage__file_path))
except:
    fs = FileStorage()
    print(type(fs._FileStorage__file_path))

try:
    print(type(FileStorage._FileStorage__objects))
except:
    fs = FileStorage()
    print(type(fs._FileStorage__objects))

fs = FileStorage()
print(type(fs.all))
print(type(fs.all()))
