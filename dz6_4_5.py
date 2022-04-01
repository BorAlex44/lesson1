import json
import sys
sys.path.append("c:/Users/Александр/PycharmProjects/Lesson6/")

all_names = []
all_surnames = []
all_middle_names = []
all_hobbies = []

path_1 = sys.argv[1]
path_2 = sys.argv[2]
path_3 = sys.argv[3]

everything = ["all_names", "all_surnames", "all_middle_names", "all_hobbies"]

with open(path_1, 'r', encoding='utf-8') as f1:
    with open(path_2, 'r', encoding='utf-8') as f2:
        for line in f1:
            all_surnames.append(line.split(',')[0])
            all_names.append(line.split(',')[1])
            all_middle_names.append(line.split(',')[2].strip())
        for line in f2:
            for el in line.split(','):
                all_hobbies.append(el.strip())
all_lists = [all_names, all_surnames, all_middle_names, all_hobbies]
parsing_data = {k: v for k, v in zip(everything, all_lists)}

with open(path_3, 'w', encoding='utf-8') as f:
    json.dump(parsing_data, f, ensure_ascii=False)
