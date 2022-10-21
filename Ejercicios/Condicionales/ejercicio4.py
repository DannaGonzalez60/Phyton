#4.Solicitarcinco (5)notas de 0.0 a 5.0 a un estudiante y calcular promedio. Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0.

CANTIDAD_NOTAS=5
num = []

for i in range(CANTIDAD_NOTAS):
    numero = float (input(f"Ingresa el numero {i + 1}: "))

    if numero <=5 and numero >= 0: 
        num.append(numero)
        total=(sum(num)/CANTIDAD_NOTAS)

    if numero < 0 or numero > 5:
        print(f"el número {i} no es un numero establecido entre rangos")
    
    if total >= 3:
        print("El estudiante ha aprobado")

    if total<= 3:
        print("El estudiante ha reprobado")

    print(f"El promedio fue de:{total}")