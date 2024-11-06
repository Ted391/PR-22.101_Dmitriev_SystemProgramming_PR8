class TriangleChecker:
    def __init__(self, a, b, c):
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            raise ValueError("Нужно вводить только числа!")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("С отрицательными числами ничего не выйдет!")
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

# Ввод данных

while True:
    try:
        a = float(input("Введите первую сторону треугольника: "))
        b = float(input("Введите вторую сторону треугольника: "))
        c = float(input("Введите третью сторону треугольника: "))

        triangle = TriangleChecker(a, b, c)
        print(triangle.is_triangle())
    except ValueError:
        print("Нужно вводить только числа!")
    print("\n==========================\n")