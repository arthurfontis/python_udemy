import numpy as np

somaMatriz = 0
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

for m in range(matriz.shape[0]):
    for n in range(matriz.shape[1]):
        somaMatriz += matriz[m][n]
        
print(somaMatriz)