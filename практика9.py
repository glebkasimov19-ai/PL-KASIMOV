# Блок А 
# Задача 5
def print_digits_reverse(n):
    if n == 0:
        return
    else:
        print(n % 10)
        print_digits_reverse(n // 10)

# Пример использования
N = int(input("Введите натуральное число N: "))
print_digits_reverse(N)
