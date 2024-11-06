class Soda:
    def __init__(self, additive=None): # Присваивание значения None параметру additive обозначает, что этот параметр необязательный и по умолчанию добавка отсутствует
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            return f"Газировка и {self.additive}"
        else:
            return "Обычная газировка"


# Ввод данных
additive = input("Введите добавку либо не вводите ничего, если она не требуется: ")

soda = Soda(additive)
print(soda.show_my_drink())
