# Вариант 7

# Задача 7.1
N = int(input("Введите количество элементов: "))
x = []
for i in range(N):
    x.append(int(input("x[" + str(i) + "] = ")))
sum_even = 0
prod_odd = 1
for i in range(N):
    if i % 2 == 0:                                     
        sum_even += x[i]
    else:                                               
        prod_odd *= x[i]
print("Сумма элементов с четными номерами:", sum_even)
print("Произведение элементов с нечетными номерами:", prod_odd)

# Задача 7.2
min_i = 0
max_i = 0
for i in range(1, N):                                    
    if x[i] < x[min_i]:
        min_i = i
    if x[i] > x[max_i]:
        max_i = i
x[min_i], x[max_i] = x[max_i], x[min_i]                 
print("Массив после обмена min и max:", x)
