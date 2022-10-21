#. 6.Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

asterisco= ["*","**","***","****","*****",]
cont=0
while cont<= 4 :
    print(asterisco[cont])
    cont=cont+1
while cont>= 1 :
    print(asterisco[cont-1])
    cont=cont-1

