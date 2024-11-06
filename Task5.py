class RealString:
    def __init__(self, string):
        self.string = string  

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        if isinstance(other, (RealString, str)):
            return len(self) == len(other)
        return NotImplemented

try:
    userInput1 = input("Введите строку: ")
    realString1 = RealString(userInput1)

    userInput2 = input("Введите еще одну строку для сравнения: ")
    realString2 = RealString(userInput2)

    print(f"Длина первой строки: {len(realString1)}")
    print(f"Длина второй строки: {len(realString2)}")

    if realString1 == realString2:
        print("Строки равны по длине.")
    elif len(realString1) < len(realString2):
        print("Первая строка короче второй.")
    else:
        print("Первая строка длиннее второй.")

except Exception as e:
    print(f"Ошибка: {e}")
