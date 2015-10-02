palabras=["abc","xd","crm","zl","xb"]

lista1=[]
lista2=[]

for palabra in palabras:
    if palabra[0] =="x":
        lista1.append(palabra)
    else:
        lista2.append(palabra)

lista_ordenada=sorted(lista1)+sorted(lista2)
print lista_ordenada