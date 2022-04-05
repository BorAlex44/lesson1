import os
dir_path = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folder in dir_path.items():
    if os.path.exists(root):
        print('Такая пака уже существует!!!!')
    else:
        for folder in folder:
            path = os.path.join(root, folder)
            os.makedirs(path)
