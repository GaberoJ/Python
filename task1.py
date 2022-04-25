with open('nginx_logs.txt', 'r') as f:
    a = []
    line = f.readline()
    while line:
        num = line.split()
        a.append((num[0], num[5].replace('"', ''), num[6]))
        line = f.readline()

for i in a[:8]:
    print(i)

print(f'Длина списка: {len(a)}')