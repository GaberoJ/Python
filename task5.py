from time import perf_counter
from sys import getsizeof

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# решение в лоб:
start_time = perf_counter()
result = []
for el in src:
    if src.count(el) == 1:
        result.append(el)

print(f'Время кода при решении в лоб: {perf_counter() - start_time} Место в памяти: {getsizeof(result)}')
print(*result)

# решение с использованием генератора:
start_time = perf_counter()
result = (el for el in src if src.count(el) == 1)
print(f'Время кода с использованием генератора: {perf_counter() - start_time} Место в памяти:  {getsizeof(result)}')
print(*result)

# решение с использованием list comprehension:
start = perf_counter()
result = [el for el in src if src.count(el) == 1]
print(f'Время кода с использованием list comprehension: {perf_counter() - start} Место в памяти: {getsizeof(result)}')
print(*result)

# Самый выгодный вариант и по времени, и по памяти в данной задаче - генератор