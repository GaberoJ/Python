info = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(info)):
    words = info[i].split()
    print('Привет ', words[-1].lower().capitalize())