def thesaurus_adv(*args):
    out_dict = {}
    for elem in args:
        name, surname = elem.split()
        if not out_dict.get(surname[0]):
            out_dict[surname[0]] = {name[0]: [elem]}
        elif not out_dict[surname[0]].get(name[0]):
            (out_dict[surname[0]])[name[0]] = [elem]
        else:
            (out_dict[surname[0]])[name[0]].append(elem)
    return out_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
