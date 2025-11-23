import math

#открытие файла
with open("KASIMOV_GROUP(УБ-52)_vvod.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

#7.1 
arr = list(map(int, lines[0].split()))

n1 = int((-1 + math.sqrt(1 + 8 * len(arr))) / 2)

matrix1 = [[0] * n1 for _ in range(n1)]

k = 0
for i in range(n1):
    for j in range(i, n1):
        matrix1[i][j] = arr[k]
        matrix1[j][i] = arr[k]
        k += 1

#7.2 
pos = 1
n2 = int(lines[pos])
pos += 1

matrix2 = []
for _ in range(n2):
    matrix2.append(list(map(int, lines[pos].split())))
    pos += 1

diagonal = [matrix2[i][i] for i in range(n2)]
trace = sum(diagonal)

if trace != 0:
    matrix2 = [
        [x / trace for x in row] if i % 2 == 0 else row
        for i, row in enumerate(matrix2)
    ]

#сохранение данных в новый файл
with open("KASIMOV_GROUP(УБ-52)_vivod.txt", "w", encoding="utf-8") as f:

    f.write("Задача 7.1 восстановленная симметричная матрица:\n")
    for row in matrix1:
        f.write(" ".join(map(str, row)) + "\n")

    f.write("\nЗадача 7.2 диагональные элементы:\n")
    f.write(" ".join(map(str, diagonal)) + "\n")

    f.write(f"След матрицы: {trace}\n")

    f.write("\nПреобразованная матрица:\n")
    for row in matrix2:
        f.write(" ".join(map(str, row)) + "\n")
