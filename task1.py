import re


def email_parse(email_address):
    email_dict = {}
    EMAIL_RE = re.compile(r'\w*@\w*[^\.]\.\w*')
    if EMAIL_RE.match(email_address):
        email_dict.setdefault('username', email_address.split('@')[0])
        email_dict.setdefault('domain', email_address.split('@')[1])
    if not EMAIL_RE.match(email_address):
        raise ValueError(f'wrong email: {email_address}')
    return email_dict


print(email_parse('helloworld@gmail.com'))
print(email_parse('helloworld@gmailcom'))
