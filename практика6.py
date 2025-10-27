# Вариант 7

# Задача 7.1
n = int(input("Введите количество элементов: "))
a = []
for i in range(n):
    a.append(int(input("a[" + str(i) + "] = ")))
sum_even = 0
prod_odd = 1
for i in range(n):
    if i % 2 == 0:                                     
        sum_even += a[i]
    else:                                               
        prod_odd *= a[i]
print("Сумма элементов с четными номерами:", sum_even)
print("Произведение элементов с нечетными номерами:", prod_odd)

# Задача 7.2
min_i = a.index(min(a))
max_i = a.index(max(a))

a[min_i], a[max_i] = a[max_i], a[min_i]

print("После обмена:", a)

