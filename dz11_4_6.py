class EquipmentWarehouse:
    __warehouse = []
    __quantity = {}

    def entrance(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise Exception('Этот товар не может быть принят на склад оргтехники')
        self.__warehouse.append(equipment)
        if self.__quantity.get(equipment.class_type) is not None:
            self.__quantity[equipment.class_type] += 1
        else:
            self.__quantity.setdefault(equipment.class_type, 1)

    def general_report(self):
        for item in self.__warehouse:
            print(item)

    def quantity_report(self):
        for k, v in self.__quantity.items():
            print(f'{k}: {v}шт.')


class OfficeEquipment:
    def __init__(self, class_type: str, model: str, cost: float, sn: str):
        self.class_type = str(class_type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f'{self.class_type} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, model: str, cost: float, sn: str, color: bool):
        self.color = color
        super().__init__('Принтер', model, cost, sn)


class Scanner(OfficeEquipment):
    def __init__(self, model: str, cost: float, sn: str, dpi: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)


class Copier(OfficeEquipment):
    def __init__(self, model: str, cost: float, sn: str, color: bool, velosity: int):
        self.color = color
        self.velosity = velosity
        super().__init__('Копир', model, cost, sn)


if __name__ == '__main__':
    printer01 = Printer('Canon PIXMA G640', 8500.50, 'N6SS549876548', True)
    printer02 = Printer('HP LaserJet Pro M28w', 10500, 'FG64855SFG5', False)
    scanner01 = Scanner('Epson', 7000, '65482321FF5', '4800x4800')
    scanner02 = Scanner('Canon', 7700.45, '31313131FFF', '2400x2400')
    copier01 = Copier('Canon PIXMA MG2540S', 5600.99, 'FG8#HHHF', True, 8)
    copier02 = Copier('Brother MFC-L2720DWR', 25000, '9BB654852133', False, 30)
    copier03 = Copier('HP LaserJet M132nw', 14604.20, '9BB654848554', False, 22)

    equipmentWarehouse = EquipmentWarehouse()
    equipmentWarehouse.entrance(printer01)
    equipmentWarehouse.entrance(printer02)
    equipmentWarehouse.entrance(scanner01)
    equipmentWarehouse.entrance(scanner02)
    equipmentWarehouse.entrance(copier01)
    equipmentWarehouse.entrance(copier02)
    equipmentWarehouse.entrance(copier03)

    equipmentWarehouse.general_report()
    equipmentWarehouse.quantity_report()
