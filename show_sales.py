import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        for line in f.readlines():
            print(line.replace('\n', ''))

    if len(sys.argv) == 2:
        for line in f.readlines()[int(sys.argv[1]) - 1:]:
            print(line.replace('\n', ''))

    if len(sys.argv) == 3:
        for line in f.readlines()[int(sys.argv[1]) - 1:int(sys.argv[2])]:
            print(line.replace('\n', ''))