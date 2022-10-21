#6.Solicitar tres números al usuario e imprimirlos en orden descendente (de mayor a menor).

CANTIDAD_NUMEROS=3
num=[]
for i in range(CANTIDAD_NUMEROS) :
    numeros= int(input(f"Ingresa el número {i + 1}: "))
    num.append(numeros)

print(sorted(num,reverse=True))