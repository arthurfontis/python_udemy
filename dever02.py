import numpy as np

lista = []
soma = 0
for _ in range(5):
    nmr = int(input())
    lista.append(nmr)
    
for i in lista:
    soma += i
    
print(soma)

#segundo ex

dc = {}
somaNotas = 0
for _ in range(3):
    nome = input()
    nota = float(input())
    
    dc[nome] = nota
    
for j in dc.values():
    somaNotas += j
    
media = somaNotas / 3
print(f"{media:.2f}")

# terciero ex

somaMatriz = 0
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

for m in range(matriz.shape[0]):
    for n in range(matriz.shape[1]):
        somaMatriz += matriz[m][n]
        
print(somaMatriz)