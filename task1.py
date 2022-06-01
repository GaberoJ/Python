class Data:
    user_data = ''

    def __init__(self, user_data: str):
        Data.user_data = user_data

    @classmethod
    def date_parser(cls):
        day, month, year = cls.user_data.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def validation(user_data):
        day, month, year = user_data.split('-')
        if not 1 <= int(day) <= 31:
            return f'Неверная дата: {user_data}'
        if not 1 <= int(month) <= 12:
            return f'Неверная дата: {user_data}'
        return f'Date: {day}-{month}-{year}'


example = Data('12-05-2013')

print('day: ', example.date_parser()[0], type(example.date_parser()[0]))
print('month: ', example.date_parser()[1], type(example.date_parser()[1]))
print('year: ', example.date_parser()[2], type(example.date_parser()[2]))
print()
print(Data.validation('30-07-2007'))
print(Data.validation('45-07-2007'))


