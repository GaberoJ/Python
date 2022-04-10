start_list = ['в', '5', 'часов', '7', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in start_list:
    if item.isdigit():
        start_list[start_list.index(item)] = '"{:02}"'.format(int(item))
    elif '-' in item:
        start_list[start_list.index(item)] = '"{:03}"'.format(int(item))
    elif '+' in item:
        start_list[start_list.index(item)] = '"+{:02}"'.format(int(item))


result = ' '.join(start_list)
print(result)