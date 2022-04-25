import sys

info = {}
users = []

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', 'r', encoding='utf-8') as userf:
        line = userf.readline()
        while line:
            info.setdefault(line.replace('\n', ''))
            users.append(line)
            line = userf.readline()

    with open('hobby.csv', 'r', encoding='utf-8') as hobbyf:
        line = hobbyf.readline()
        i = 0
        while line:
            if len(users) < i + 1:
                sys.exit(1)
            info[users[i].replace('\n', '')] = line.replace('\n', '')
            i += 1
            line = hobbyf.readline()

    for k, v in info.items():
        f.write(f'{k}: {v}\n')
