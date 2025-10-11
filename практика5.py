#Вариант 1
print("Введите строку:")
s = input()

words = s.split(' ')  
count = 0

for i in range(len(words)): 
    word = words[i]
    if len(word) > 0 and (word[0] == 'е' or word[0] == 'Е'): 
        count = count + 1  

print("Количество слов, начинающихся с 'е':", count)



#Вариант 2
print("Введите строку:")
s = input()

count = s.count(':')        
new_s = s.replace(':', '%') 

print("Новая строка:", new_s)
print("Количество замен:", count)




#Вариант 3
print("Введите строку:")
s = input()

count = s.count('.')       
new_s = s.replace('.', '') 
print("Новая строка:", new_s)
print("Удалено символов '.':", count)






#Вариант 4
print("Введите строку:")
s = input()

count = s.count('а')       
new_s = s.replace('а', 'о')
length = len(new_s)        

print("Новая строка:", new_s)
print("Количество замен:", count)
print("Длина строки:", length)




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






#Вариант 6
print("Введите строку:")
s = input()

count = s.count('a')       
new_s = s.replace('a', '') 

print("Новая строка:", new_s)
print("Удалено символов 'a':", count)






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
