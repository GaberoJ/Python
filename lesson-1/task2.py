# a
def sum_list_1(dataset: list) -> int:
    summ_numbers = []

    for number in dataset:
        summ = 0
        number1 = number
        while number1 != 0:
            summ += number1 % 10
            number1 = number1 // 10
        if summ % 7 == 0:
            summ_numbers.append(number)
    total = sum(summ_numbers)
    return total  # Верните значение полученной суммы


# b
def sum_list_2(dataset: list) -> int:
    for i in range(len(my_list)):
        my_list[i] += 17

    new_summ_numbers = []
    for number in my_list:
        summ = 0
        number2 = number
        while number2 != 0:
            summ += number2 % 10
            number2 = number2 // 10
        if summ % 7 == 0:
            new_summ_numbers.append(number)
    total_2 = sum(new_summ_numbers)

    return total_2  # Верните значение полученной суммы


# c
def sum_list_3(dataset: list) -> int:
    total_3 = 0
    for number in my_list:
        summ_of_digits = 0
        number1 = number
        while number1 != 0:
            summ_of_digits += number1 % 10
            number1 = number1 // 10
        if summ_of_digits % 7 == 0:
            total_3 += number

    return total_3  # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []  # Соберите нужный список по заданию

    for i in range(1, 1000, 2):
        cube = i ** 3
        my_list.append(cube)

    print('Задание 2.а')
    result_1 = sum_list_1(my_list)
    print('Сумма: ', result_1)
    print()

    print('Задание 2.b')
    result_2 = sum_list_2(my_list)
    print('Сумма:', result_2)
    print()

    print('Задание 2.c')
    result_3 = sum_list_3(my_list)
    print('Сумма:', result_3)





