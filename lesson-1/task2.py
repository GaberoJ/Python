'''
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из 
  этого списка, сумма цифр которых делится нацело на 7. 
* Решить задачу под пунктом b, не создавая новый список.)
'''




# a
def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
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
    print('Числа, сумма цифр которых делится на 7 нацело: ', summ_numbers)
    return total  # Верните значение полученной суммы




# b
def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, 
        сумма цифр которых делится нацело на 7"""

    my_list_copy = dataset[:]
    for i in range(len(my_list_copy)):
        my_list_copy[i] += 17
    print('Список кубов нечетных чисел от 1 до 1000 (+ 17): ', my_list_copy)

    new_summ_numbers = []
    for number in my_list_copy:
        summ = 0
        number2 = number
        while number2 != 0:
            summ += number2 % 10
            number2 = number2 // 10
        if summ % 7 == 0:
            new_summ_numbers.append(number)
    print('Числа, сумма цифр которых делится на 7 нацело: ', new_summ_numbers)
    total_2 = sum(new_summ_numbers)

    return total_2 # Верните значение полученной суммы




if __name__ == '__main__':
    my_list = []# Соберите нужный список по заданию

    for i in range(1, 1000):
        if i % 2 != 0:
            cube = i ** 3
            my_list.append(cube)
    print('Список кубов нечетных чисел от 1 до 1000: ', my_list)
    print()

    print('Задание 2.а')
    result_1 = sum_list_1(my_list)
    print('Сумма: ', result_1)
    print()

    print('Задание 2.b')
    result_2 = sum_list_2(my_list)
    print('Сумма:', result_2)






