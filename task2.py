with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    a = {}
    max_count = 0
    line = f.readline()
    while line:
        num = line.split()
        if num[0] in a:
            a[num[0]] += 1
        a.setdefault(num[0], 1)
        if a[num[0]] > max_count:
            max_count = a[num[0]]
            ip_of_max_count = num[0]
        line = f.readline()

print(f'IP спамера: {ip_of_max_count}, количество отправленных запросов: {max_count}')


