class KgToPounds:
    def __init__(self, kg):
        self.kg = kg 

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)) and new_kg > 0:
            self.__kg = new_kg
        else:
            raise ValueError("Килограммы должны быть положительным числом")

    def to_pounds(self):
        return self.__kg * 2.205

while True:
    try:
        weight_in_kg = float(input("Введите вес в килограммах: "))
        weight_in_pounds = KgToPounds(weight_in_kg)

        print(f"Вес в килограммах: {weight_in_pounds.kg:.2f}")
        print(f"Вес в фунтах: {weight_in_pounds.to_pounds():.2f}")

    except ValueError as e:
        print(f"Ошибка: {e}")

