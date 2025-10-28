coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darling': 14}

print(coleta['Aedes aegypt'])
print('-' * 22)

coleta['Rhodnius montenegrensis'] = 11

print(coleta)
print('-' * 22)

del(coleta)['Aedes albopictus']
print(coleta)

print('-' * 22)

print(coleta.items())
print('-' * 22)

print(coleta.keys())
print(coleta.values())
print('-' * 22)

coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
print(coleta2)

coleta.update(coleta2)
print(coleta)

print('-' * 22)
print(coleta.items())

for especie, num_especie in coleta.items():
    print(f"Espécie: {especie}, número de espécies coletados: {num_especie}")
    
    
#conj


print('-' * 22)
biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo', 'ácidos nucleicos' , 'carboidrato', 'carboidrato')
print(biomoleculas)
print(set(biomoleculas))

c1 = {1,2,3,4,5}
c2 ={3,4,5,6,7}

c3 = c1.intersection(c2)
print(c3)

print(c1.difference(c2))
print(c2.difference(c1))