# 4.Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.

CANTIDAD=10
numeros=[]
for i in range(CANTIDAD) :
    numero= int(input(f"Ingresa el número {i + 1}: "))
    print(numero)
    numeros.append(numero)
    suma=sum(numeros)
    promedio=(sum(numeros)/CANTIDAD)
print(f"la suma es: {suma} el promedio es: {promedio}")