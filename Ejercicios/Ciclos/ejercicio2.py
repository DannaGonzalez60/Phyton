# 2.Escriba un programa para encontrar la suma de los primeros 20 números naturales. El total es 210. 

CANTIDAD_NUMEROS=20
num=[]
for i in range(CANTIDAD_NUMEROS) :
    num.append(i+1)
    print(num)

print(sum(num))
