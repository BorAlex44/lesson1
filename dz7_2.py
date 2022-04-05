import yaml
import os

my_dict = {'my_project':
       [{'settings':[
            '__init__.py', 'dev.py', 'prod.py'
        ], },
           {'mainapp': [
               '__init__.py', 'models.py', 'views.py', {'templates': [{
                   'mainapp':['base.html', 'index.html']}]
               }]},
           {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
               'authapp': ['base.html', 'index.html']}]
            }]}
        ]}
file = open('config.yaml', 'w')
file.write(yaml.dump(my_dict))
file.close()

with open('config.yaml') as yaml_file:
    my_dict = yaml.safe_load(yaml_file)


def create_data(data):
    for folder, data_tmp in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for elem in data_tmp:
            if isinstance(elem, dict):
                create_data(elem)
            else:
                if not os.path.exists(elem):
                    if '.' in elem:
                        with open(elem, 'w') as new_file:
                            new_file.write('')
    else:
        os.chdir('../')


create_data(my_dict)

