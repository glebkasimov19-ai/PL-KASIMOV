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