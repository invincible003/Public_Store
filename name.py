import os

directory_path = "Wallpaper"

files = os.listdir(directory_path)

start_count = 0

for file in files:
    file_name = os.path.join(directory_path, file)
    new_name = f"nature {start_count}.jpg"
    new_file_path = os.path.join(directory_path, new_name)
    os.rename(file_name, new_file_path)
    start_count += 1