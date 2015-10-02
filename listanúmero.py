
numeros=[1,23,67,67,8,8,5,9,5,3,0,12,12,23,45]

for elementos in numeros:
    posicion=numeros.index(elementos)
    if posicion !=len(numeros)-1:
        if elementos==numeros[posicion+1]:
            numeros.remove(elementos)
print numeros