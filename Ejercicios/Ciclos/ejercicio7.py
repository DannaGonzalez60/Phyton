# 7.Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número. El patrón como:
# 1
# 12
# 123
# 1234
# 12345

n = int(input("ingresa el numero de filas deseaadas:")) 
x=1 
y=1 
z=1
frase = ''  
for x in range(1,n+1):
    for z in range(1,x+1):
        frase+=(str(y)+(' '))
        y+=1
        print(frase)    