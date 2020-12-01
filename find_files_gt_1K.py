import os

min_size = 5000

start_dir = '.'

for folder, subs, files in os.walk(start_dir):
    for file_name in files:
        file_path = os.path.join(folder, file_name)
        file_size = os.path.getsize(file_path)
        if file_size >= min_size:
            print(f"{file_size:8d} {file_path}")
