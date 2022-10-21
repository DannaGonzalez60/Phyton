#3.Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir los resultados.

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

if a > b:
    print("El numero mayor es", a)
if b > a:
    print("El numero mayor es", b)
if a == b:
    print("Los numeros son iguales")