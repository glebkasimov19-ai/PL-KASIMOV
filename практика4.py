# Задачи
#1.
A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if A <= B:
    while A <= B:
        print(A)
        A = A + 1
else:
    print("Ошибка: А должно быть меньше или равно B")


#2.
A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if A < B:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, B - 1, -1):
        print(i)


#3.
A = int(input("Введите число A:"))
B = int(input("Введите число B:"))

for i in range(A, B - 1, -1):
    if i % 2 != 0:
        print(i)


#4.
N = int(input("Введите число N:"))
print(sum(int(input())for _ in range(N)))


#5.
n = int(input("Введите число n:"))
s = 0
for i in range(1, n + 1):
    s = s + i ** 3
print(s)

<<<<<<< HEAD
#7.
n = int(input("n = "))

sum = 0       # здесь будем накапливать сумму факториалов
faсtorial = 1   # здесь будем хранить текущий факториал (начинаем с 1!)

for i in range(1, n + 1):
    faсtorial = faсtorial * i   # например: 2! = 1! * 2 → 1*2=2
    sum = sum + faсtorial   # добавляем к общей сумме

print("Ответ:", sum)
=======


#7.
n = int(input("n = "))

sum = 0       
faсtorial = 1  

for i in range(1, n + 1):
    faсtorial = faсtorial * i  
    sum = sum + faсtorial   

print("Ответ:", sum)
