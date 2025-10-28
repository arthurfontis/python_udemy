import numpy as np

matriz = np.array([[2,3,1], [4,5,7]])

print(matriz)

print('-' * 10)

print(matriz.shape)

print('-' * 10)

print(matriz[0])
print(matriz[1])


print('-' * 10)

print(matriz[0][0])
print(matriz[1][0])

print('-' * 10)

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])
