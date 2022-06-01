class Warehouse:
    division_a = []
    division_b = []
    division_c = []

    def __call__(self, *args, **kwargs):
        for k, v in Warehouse.__dict__.items():
            if not str(k).startswith('_'):
                print(f'{k}: {v}')


class OfficeEquipment:
    def __init__(self, model, cost, quantity):
        self.model = model
        self.cost = cost
        self.quantity = quantity
        if type(self.cost) != int:
            raise ValueError(f'Введена неверная цена у модели {self.model}')
        elif type(self.quantity) != int:
            raise ValueError(f'Введено неверное количество у модели {self.model}')

    def transfer_to_warehouse(self, warehouse):
        for el in Warehouse.__dict__:
            if el == warehouse:
                Warehouse.__dict__[el].append(self.__dict__)

    def __str__(self):
        return str(self.__dict__)


class Printer(OfficeEquipment):
    def __init__(self, model, cost, quantity, laser=True):
        super().__init__(model, cost, quantity)
        self.laser = laser


class Scanner(OfficeEquipment):
    def __init__(self, model, cost, quantity, type_of_paper):
        super().__init__(model, cost, quantity)
        self.type_of_paper = type_of_paper


class Xerox(OfficeEquipment):
    def __init__(self, model, cost, quantity, remote_connection):
        super().__init__(model, cost, quantity)
        self.remote_connection = remote_connection


info = Warehouse()
printer = Printer('Epson', 25000, 3)
scanner = Scanner('Canon', 18000, 12, 'plain paper')
xerox = Xerox('HP', 34000, 2, True)
another_equipment = OfficeEquipment('Lenovo', 12000, 1)

printer.transfer_to_warehouse('division_a')
scanner.transfer_to_warehouse('division_b')
xerox.transfer_to_warehouse('division_c')
another_equipment.transfer_to_warehouse('division_b')

info()
