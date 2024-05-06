import os

if not os.path.exists("New Folder"):
    os.mkdir("New Folder")

for i in range(0, 100):
    os.mkdir(f"New Folder/project {i+1}")