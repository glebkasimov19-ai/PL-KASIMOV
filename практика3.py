# Задание 1 ( 1.1 )
a = 2
b = 5
c = 1

result = []

if 1 <= a <= 3:
    result.append(a)
if 1 <= b <= 3:
    result.append(b)
if 1 <= c <= 3:
    result.append(c)

print(result)



# Задача 2 ( Вариант 1 )

# Значения
a = 3
b = 5

if a < b:
    x = a + b
elif a > b:
    x = a - b
else:  # a == b
    x = 1

print(x)




# Задание 3 
# 1. Задание : Сравнение двух чисел и вывод наибольшего

print('Введите A:')
A = input ()
print('Введите B:')
B = input ()
if A > B:
    print (A)
else:
    if A < B:
        print (B) 


# 2. Задание : Проверка числа на чётность и вывод результата
def check_even(number):
    if number % 2 == 0:
        print(f"{number} — чётное число")
    else:
        print(f"{number} — нечётное число")



# 3. Задание : Разделение числа на чётные и нечётные цифры
def split_digits(number):
    even_digits = []
    odd_digits = []
    for digit in str(number):
        if int(digit) % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
    print(f"Чётные цифры: {even_digits}")
    print(f"Нечётные цифры: {odd_digits}")



# 4. Задание : Проверка числа на простоту
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# 5. Задание : Вычисление среднего арифметического трёх чисел
def average_of_three(a, b, c):
    return (a + b + c) / 3
num = int(input("Введите число: "))
check_even(num)
split_digits(num)
print(f"{num} — простое число? {is_prime(num)}")

a = int(input("Введите первое число для среднего арифметического: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print(f"Среднее арифметическое: {average_of_three(a, b, c)}")