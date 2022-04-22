def gen_uneven_numbers(user_number):
    numbers_gen = (x for x in range(1, user_number + 1, 2))
    for el in numbers_gen:
        print(el)


print(gen_uneven_numbers(15))
