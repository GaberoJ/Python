price = [57.8, 46.51, 97, 123.45, 13, 84.07, 15.00, 0.24, 1.99, 0, 12.86, 54.7, 12.9, 2.03, 111.10]

for item in price:
    if not str(item).isdigit():
        cent = str(item).split('.')
        correct_cent = int(cent[-1])
        if len(cent[-1]) == 1:
            correct_cent = int('{}0'.format(correct_cent))
    else:
        correct_cent = 0
    print(int(item), 'руб ', '{:02} коп'.format(correct_cent), end=', ')

# Цены по возрастанию, без создания нового списка
print()
print('id изначального списка: ', id(price))
price.sort()
print(price, ' id отсортированного списка ', id(price))

# Новый список
price_sorted_reverse = sorted(price, reverse=True)
print(price_sorted_reverse)

# 5 самых дорогих товаров по возрастанию
print(sorted(price_sorted_reverse[:5]))