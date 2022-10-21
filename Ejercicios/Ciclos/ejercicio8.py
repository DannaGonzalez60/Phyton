# 8.Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1.

pi=int(input("Ingrese la cantidad de lineas que desee:"))
num=int(input("Ingrese el numero para imprimir:"))
for i in range(pi):
		x = pi - i - 1
		z = i * 2 + 1
		print (" " * x + str(num) * z)