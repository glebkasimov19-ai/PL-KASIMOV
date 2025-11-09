# Блок А 
# Задача 5
def print_digits_reverse(n):
    if n == 0:
        return
    else:
        print(n % 10)
        print_digits_reverse(n // 10)

N = int(input("Введите натуральное число N: "))
print_digits_reverse(N)

# Блок Б
# Задача 3
def f():
    if not hasattr(f, 'arr'):
        f.arr = []
    n = int(input())
    if n == 0:
        print("Результат:")
        for i in range(0, len(f.arr), 2):
            print(f.arr[i])
        f.arr = []
        return
    f.arr.append(n)
    f()
f()