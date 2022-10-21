#1.Par o impar. Solicitar número al usuario y determinar si es par, impar o es cero. 

num = int(input("Ingresa el numero para saber si es par o inpar: "))

if num != 0:
    print("El numero es diferente de 0")
else:
    print("el numero es 0")
if num % 2 == 0:
    print("El numero es par")
if num % 3 == 0:
    print("El numero es inpar") 
