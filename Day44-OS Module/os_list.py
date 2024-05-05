import os

folders = os.listdir("New Folder")

print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"New Folder/{folder}"))