#2.Solicitar número al usuario y determinar si es negativo, positivo o cero.

num = int(input("Ingresa el numero para saber si es negativo o positivo: "))

if num == 0:
    print("El numero es", num)
if num > 0:
    print("El numero es positivo")
if num < 0:
    print("El numero es negativo")