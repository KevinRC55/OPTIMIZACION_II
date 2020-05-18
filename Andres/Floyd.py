
import numpy as np

def impimir_bonito(a):
    for f in a:
        print(f)

n = int(input("Introducir numero de nodos: "))

ma = []  # Matriz de distancias
mb = []  # Matriz de recorridos

#Rellenar la matriz de distancias , distancias asi mismas valen 0 por defecto
for i in range(n):
    ma.append([])
    for j in range(n):
        if (i==j):
            dis=0
            ma[i].append(dis)
        else:
            dis = float(input(f"Indique distancia {i}{j}: "))
            ma[i].append(dis)

#Construir la matriz de recorridos
for i in range(n):
    mb.append([])
    for j in range(n):
            marca = j
            mb[i].append(marca)

mb = np.array(mb)
ma = np.array(ma)

#Floyd
for k in range(n):
    print(f"Iteracion: {k}")
    print(ma)#Esto imprime la matriz de distancias
    for i in range(n):
        for j in range(n):
            v = ma[i][j]
            ma[i][j] = min(ma[i][j],ma[i][k] + ma[k][j])
            if(ma[i][j]!=v):
                mb[i][j]=k

print("Matriz de distancias final")
impimir_bonito(ma)

print("Matriz de recorridos final ")
impimir_bonito(mb)

