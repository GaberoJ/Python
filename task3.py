import sys
import json

info = {}
users = []

with open('users.csv', 'r', encoding='utf-8') as f:
    users_text = f.readlines()
    for line in users_text:
        info.setdefault(line.replace('\n', '').replace(',', ' '))
        users.append(line.replace('\n', '').replace(',', ' '))

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby_text = f.readlines()
    i = 0
    for line in hobby_text:
        if len(users) < i + 1:
            sys.exit(1)
        info[users[i]] = line.replace('\n', '').replace(',', ', ')
        i += 1

# Сохранение и чтение словаря в отдельном файле
with open('dict.json', 'w', encoding='utf-8') as jf:
    json.dump(info, jf)

with open('dict.json', 'r', encoding='utf-8') as jf:
    result_info = json.load(jf)

print(f'{result_info}\n{type(result_info)}')