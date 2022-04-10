'''
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

def transform_string(number: int) -> str:
    numbers = []
    exception = [11, 12, 13, 14]
    numbers.append(str(number))
    if number in exception:
        string = str(number) + ' Процентов'
    elif numbers[0][-1] == '1':
        string = str(number) + ' Процент'
    elif numbers[0][-1] == '2' or numbers[0][-1] == '3' or numbers[0][-1] == '4':
        string = str(number) + ' Процента'
    else:
        string = str(number) + ' Процентов'
    return string


if __name__ == '__main__':
    for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
        print(transform_string(n))
