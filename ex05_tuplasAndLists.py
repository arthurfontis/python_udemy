tupla = ('Homo sapiens' , 'Canis familiaris', 'Felis catus')
print(tupla)
print(tupla[0])

print(tupla.index('Canis familiaris'))

for elemento in tupla:
    print(elemento)
    
lista1 = ['Homo sapiens' , 'Canis familiaris', 'Felis catus']
lista2 = ['Xenopus laevis', 'Ailuropa melanoleuca']
lista3 = lista1 + lista2

print(lista3)

lista2_2 = lista2 * 2
print(lista2_2)

print(lista1[0])
print(lista1[0:2])

lista1.append('Gorila gorila')
print(lista1)

lista1.remove('Felis catus')
print(lista1)

del(lista1)
#print(lista1)

for item in lista2_2:
    print(item)

