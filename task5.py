import sys
import os


def csv_check(*args):
    info = {}
    users = []
    with open(os.path.abspath(sys.argv[3]), 'w', encoding='utf-8') as f:
        with open(os.path.abspath(sys.argv[1]), 'r', encoding='utf-8') as userf:
            line = userf.readline()
            while line:
                info.setdefault(line.replace('\n', ''))
                users.append(line)
                line = userf.readline()

        with open(os.path.abspath(sys.argv[2]), 'r', encoding='utf-8') as hobbyf:
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


csv_check()

# Для проверки через консоль использовал: python .\task5.py .\users.csv .\hobby.csv .\users_hobby.txt

