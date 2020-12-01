import os   #  os.path
from datetime import datetime

folder = "DATA"
file = 'mary.txt'

file_path = os.path.join(folder, file)
print("file_path: {}\n".format(file_path))

print("file name:", os.path.basename(file_path))
print("dir name:", os.path.dirname(file_path))
print("absolute path:", os.path.abspath(file_path))

file_size = os.path.getsize(file_path)
file_raw_timestamp = os.path.getmtime(file_path)
print(f"file size: {file_size} file timestamp {file_raw_timestamp}")
file_timestamp = datetime.fromtimestamp(file_raw_timestamp)
print(f"file date:", file_timestamp)
print()

for thing in folder, file_path, '/', '/tmp', '/dev/null', os.path.abspath(file_path), 'mugwump':
    print(os.path.isdir(thing), os.path.isfile(thing), os.path.isabs(thing), os.path.exists(thing))
print()
