# Вариант 1

# Задача 1.1
N = int(input("Введите количество элементов: "))          
x = []                                                   
for i in range(N):                                       
    x.append(int(input("x[" + str(i) + "] = ")))         
min_elem = x[0]                                          
min_i = 0                                              
for i in range(1, N):                                   
    if x[i] < min_elem:                                 
        min_elem = x[i]                                  
        min_i = i                                        
print("Индекс минимального элемента:", min_i)            

# Задача 1.2
N = int(input("Введите количество элементов (для разделения): "))
A = []
for i in range(N):
    A.append(int(input("A[" + str(i) + "] = ")))
pos = []                                                 
other = []                                               
for i in range(N):
    if A[i] > 0:
        pos.append(A[i])                                
    else:
        other.append(A[i])                               
print("Положительные:", pos)
print("Остальные:", other)





# Вариант 2

# Задача 2.1
N = int(input("Введите количество элементов: "))          
x = []                                                   
for i in range(N):                                       
    x.append(int(input("x[" + str(i) + "] = ")))         
min_elem = x[0]                                          
min_i = 0                                                
for i in range(1, N):                                    
    if x[i] < min_elem:                                 
        min_elem = x[i]                                 
        min_i = i                                        
print("Индекс минимального элемента:", min_i)            

# Задача 2.2 
N = int(input("Введите количество элементов (для разделения): "))
A = []
for i in range(N):
    A.append(int(input("A[" + str(i) + "] = ")))
pos = []                                                 
other = []                                               
for i in range(N):
    if A[i] > 0:
        pos.append(A[i])                                 
    else:
        other.append(A[i])                               
print("Положительные:", pos)
print("Остальные:", other)






# Вариант 3

# Задача 3.1
N = int(input("Введите количество элементов массива D: "))
D = []
for i in range(N):
    D.append(int(input("D[" + str(i) + "] = ")))
s = 0
for i in range(1, N, 2):                                  
    s += D[i]
print("Сумма элементов с нечетными индексами:", s)

# Задача 3.2
for i in range(N):
    D[i] = D[i] * 2                                      
print("Преобразованный массив D:", D)







# Вариант 4

# Задача 4.1
N = int(input("Введите количество элементов: "))
x = []
for i in range(N):
    x.append(int(input("x[" + str(i) + "] = ")))
max_elem = x[0]
max_i = 0
for i in range(1, N):
    if x[i] > max_elem:
        max_elem = x[i]
        max_i = i
print("Максимальный элемент:", max_elem, "Его индекс:", max_i)

# Задача 4.2
a = []
for i in range(N):
    if x[i] % 2 == 0:
        a.append(x[i])
print("Четные элементы:", a)
print("Количество четных:", len(a))





# Вариант 5

# Задача 5.1
N = int(input("Введите количество элементов: "))
x = []
for i in range(N):
    x.append(int(input("x[" + str(i) + "] = ")))
for i in range(N - 1):                                   
    if x[i] < 0 and x[i + 1] < 0:                        
        print("Пара отрицательных:", x[i], x[i + 1])

# Задача 5.2
a = []
for i in range(N):
    if x[i] not in a:                              
        a.append(x[i])                             
print("Массив без повторов:", a)






# Вариант 6

# Задача 6.1
x = []
for i in range(10):
    x.append(int(input("x[" + str(i) + "] = ")))
max_elem = x[0]
for i in range(1, 10):
    if x[i] > max_elem:
        max_elem = x[i]
less = 0
greater = 0
for i in range(10):
    if x[i] < max_elem:
        less += 1
    elif x[i] > max_elem:
        greater += 1
print("Максимальный элемент:", max_elem)
print("Количество элементов меньше:", less)
print("Количество элементов больше:", greater)

# Задача 6.2
A = []
for i in range(10):
    A.append(int(input("A[" + str(i) + "] = ")))
s = 0
for i in range(10):
    if A[i] > 5:
        s += A[i]
print("Сумма элементов > 5:", s)





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
