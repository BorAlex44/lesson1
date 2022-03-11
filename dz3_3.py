def thesaurus(*args):
    name_dict = {}
    for name in args:
        if name_dict.get(name[0]):
            name_dict[name[0]].append(name)
        else:
            name_dict[name[0]] = [name]
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Олег", "Илья", "Ольга"))