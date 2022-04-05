import os
import shutil

dir_name = 'templates'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

folder = os.path.abspath('my_project')
new_files = []

for root, dirs, files in os.walk(folder):
    for file in files:
        if '.html' in file:
            new_files.append(os.path.join(root, file))
for path in new_files:
    folder = os.path.join(dir_name, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    new_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, new_path)
