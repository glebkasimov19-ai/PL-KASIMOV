# Пример 1 
import math 
x = 14.26

y = -1.22

z = 3.5 * 10 ** - 2

s = ((2 * math.cos(x - 2 / 3 )) / (1 / 2 + math.sin(y) ** 2)) * ( 1 + ((z ** 2) / (3 - z ** 2 / 5)))
print("s = {0:.6f}".format(s))



# Пример 2
x = -4.5

y = 0.75 * 10 ** - 4

z = -0.845 * 10 ** 2

s= (math.pow((9 + (x - y) ** 2), 1 / 3) / (x ** 2 + y ** 2 + 2)) - (math.exp(abs(x - y)) * (math.tan(z) ** 3))
print("s = {0:.5f}".format(s))



# Пример 3
x = 3.74 * 10 ** -2

y = - 0.825

z = 0.16 * 10 ** 2

s = ((1 + math.pow(math.sin(x + y), 2))/(abs(x - (2 * y / 1 + x **2 * y **2)))) * x ** (abs(y)) + math.pow(math.cos(math.atan(1 / z)), 2)
print("s = {0:.5f}".format(s))



# Пример 4
x = 0.4 * 10 ** 4 

y = - 0.875

z = -0.475 * 10 ** -3

s = (abs(math.cos(x) - math.cos(y)) ** (1 + 2 * math.pow(math.sin(y), 2))) * (1 + z + (z ** 2) / 2 + (z ** 3) / 3 + (z ** 4) / 4)
print("s = {0:.5f}".format(s))



# Пример 5
x = -15.246 

y = 4.642 * 10 ** - 2 

z = 21 

s = math.log(y ** -math.sqrt(abs(x))) * (x - y / 2) + math.pow(math.sin(math.atan(z)), 2)
print("s = {0:.3f}".format(s))


