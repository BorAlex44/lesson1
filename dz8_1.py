import re
EMAIL = re.compile(r'([a-zA-Z0-9]+)@([a-zA-Z0-9]+\.[a-z]+)')


def email_parse(email):
    found_info = EMAIL.findall(email)
    if EMAIL.match(email):
        name, adr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    return dict(username=name, domain=adr)


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
