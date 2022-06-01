class ListException(Exception):
    list_of_user_values = []
    print('Введите stop для завершения программы')

    def __init__(self):
        self.message = 'Введите число'
        super().__init__(self.message)

    def __str__(self):
        while True:
            self.user_number = input('Введите: ')
            if self.user_number == 'stop':
                break
            try:
                if int(self.user_number) or self.user_number == '0':
                    ListException.list_of_user_values.append(int(self.user_number))
            except:
                print(self.message)
        return f'Итоговый список: {str(ListException.list_of_user_values)}'


example = ListException()
print(example)
