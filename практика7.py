# Варинат 5
# Задача 5.1
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

numerator = A * D - C * B
denominator = B * D

if denominator < 0:
    numerator = -numerator
    denominator = -denominator 

g = gcd(abs(numerator), abs(denominator))
numerator //= g
denominator //= g

print(f"Результат: {numerator}/{denominator}")


#Задача 5.2
n = int(input("Введите число: "))
deliteli = []

for i in range(1, n + 1):
    if n % i == 0:
        deliteli.append(str(i))  
print(" ".join(deliteli))



# Вариант 7
# Задача 7.1
def area_rectangle(a, b):
    return a * b

def area_right_triangle(a, b):
    return (a * b) / 2

X = int(input("Введите длину стороны X: "))
Y = int(input("Введите длину стороны Y: "))
Z = int(input("Введите длину стороны Z: "))
T = int(input("Введите длину стороны T: "))

print("Фигура — прямоугольник.")
area = area_rectangle(X, Y)
print(f"Площадь прямоугольника: {area}")



# Задача 7.2
n = int(input("Введите неотрицательное целое число:"))
s = f"{n:o}"
print('0' * (10 - len(s)) + s)