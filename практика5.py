#Вариант 5
s = input("Введите строку: ")
print("Результат:", s.lower())


#Вариант 7
print("Введите строку:")
s = input()

n = len(s)
half = s[0:n//2]          

if 'n' in half:
    s = s.replace('n', '*')         

print("Результат:", s)
