from itertools import zip_longest
import json

out_dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        user_lines = users.readlines()
        hobby_lines = hobby.readlines()
        if len(user_lines) < len(hobby_lines):
            exit(1)
        for fio, hobbys in zip_longest(user_lines, hobby_lines):
            fio = fio.replace("\n", "")
            out_dict[fio] = hobbys.replace("\n", "") if hobbys else None
with open('task6_3.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f, ensure_ascii=False)
print(out_dict)