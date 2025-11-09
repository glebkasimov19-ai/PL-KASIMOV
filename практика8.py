# Вариант 5
# Задача 5.1
n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

matrix = []
print("Введите элементы матрицы построчно (через пробел):")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    matrix[i].sort()

print("\nМатрица после сортировки строк:")
for row in matrix:
    print(' '.join(map(str, row)))


# Задача 5.2
n, m = map(int, input("Введите n и m: ").split())

print("Введите элементы матрицы построчно:")
matrix = [list(map(int, input().split())) for _ in range(n)]

for row in matrix:
    j_min = min(range(m), key=lambda j: row[j])
    row[j_min] = 0 if int(row[j_min]) % 2 == 0 else 1

print("\nНовая матрица:")
for row in matrix:
    print(*row)


# Вариант 7
# Задача 7.1
import math

arr = list(map(int, input("Введите элементы верхнего треугольника через пробел: ").split()))

n = int((-1 + math.sqrt(1 + 8 * len(arr))) / 2)

matrix = [[0] * n for _ in range(n)]

k = 0
for i in range(n):
    for j in range(i, n):
        matrix[i][j] = arr[k]
        matrix[j][i] = arr[k]
        k += 1

print("\nВосстановленная симметричная матрица:")
for row in matrix:
    print(*row)


# Задача 7.2
n = int(input("Введите размер квадратной матрицы: "))

matrix = [list(map(int, input(f"Введите {i+1}-ю строку через пробел: ").split())) for i in range(n)]

diagonal = [matrix[i][i] for i in range(n)]
trace = sum(diagonal)
print("Диагональные элементы:", diagonal)
print("След матрицы:", trace)

if trace == 0:
    print("Деление на 0 невозможно, матрица не изменена.")
else:
    matrix = [[x / trace for x in row] if i % 2 == 0 else row for i, row in enumerate(matrix)]

print("Преобразованная матрица:")
for row in matrix:
    print(row)
