#Вариант 5
print("Введите строку:")
s = input()

result = ''
for i in range(len(s)):
    ch = s[i]
    if 'А' <= ch <= 'Я':          
        ch = chr(ord(ch) + 32)    
    result = result + ch

print("Результат:", result)



#Вариант 7
print("Введите строку:")
s = input()

n = len(s)
half = s[0:n//2]          
found = half.find('n')     

if found != -1:           
    new_s = s.replace('n', '*')  
else:
    new_s = s              

print("Результат:", new_s)
