# 9. Escriba un programa para calcular el factorial de un número dado.

import math

FACTORIAL= int(input("Ingrese un numero factorial: ")) 
num = []
for i in range(FACTORIAL):
    numero= i + 1
    num.append(numero)
print(math.prod(num))