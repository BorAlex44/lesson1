import os
size_files = []
for root, dirs, files in os.walk('./'):
    for file in files:
        file_path = os.path.join(root, file)
        size_files.append(os.stat(file_path).st_size)
i = 1
out_dict = {}
for _ in range(7):
    i *= 10
    out_dict[i] = 0
for file in size_files:
    out_dict[10**len(str(file))] += 1

print(out_dict)
