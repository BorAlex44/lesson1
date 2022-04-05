import os
import json
import pprint

size_file = []
for root, dirs, files in os.walk('./'):
    for file in files:
        file_path = os.path.join(root, file)
        size_file.append((file_path.split('.')[-1], os.stat(file_path).st_size))

i = 1
out_dict = {}
for _ in range(7):
    i *= 10
    out_dict[i] = (0, [])

for file in size_file:
    num, ext_list = out_dict[10**len(str(file[1]))]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    out_dict[10**len(str(file[1]))] = (num + 1, ext_list)
pprint.pprint(out_dict)

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
    json.dump(out_dict, f_json)
