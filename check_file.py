import os

path = "uploads/test.m4a"

print("File exists:", os.path.exists(path))
print("File size:", os.path.getsize(path), "bytes")