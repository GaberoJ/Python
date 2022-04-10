def naive_realisation(duration: int):
    total_time = ''
    """
    Решение задачи БЕЗ использования циклов.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    s = duration % 60
    m = duration // 60
    h = duration // 3600
    d = duration // 86400
    if duration < 60:
        total_time = str(duration) + ' сек'
    elif duration >= 60 and duration < 3600:
        total_time = f'{m} мин {s} сек'
    elif duration >= 3600 and duration < 86400:
        m = m % 60
        total_time = f'{h} час {m} мин {s} сек'
    else:
        m = m % 60
        h = h % 24
        total_time = f'{d} дн {h} час {m} мин {s} сек'
    return total_time


def one_cycle_realisation(duration):
    total_time = ''
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """

    # YOUR CODE HERE
    return total_time


if __name__ == '__main__':
    duration = 400153
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))