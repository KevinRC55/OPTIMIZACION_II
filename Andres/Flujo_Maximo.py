
from _collections import deque

def constructor_rutas(graf, o, d, rutas, n):
    nodos = deque()
    visitados = []
    graf2 = graf

    for x in range(0, n):
        f = False
        visitados.append(f)

    nodos.append(o)
    visitados[o] = True
    rutas[o] = -1

    while len(nodos) != 0:
        i = nodos.popleft()

        for j in range(0, n):
            if (visitados[j] == False) and (graf2[i][j] > 0):
                nodos.append(j)
                visitados[j] = True
                rutas[j] = i

    if visitados[d]:
        return True
    else:
        return False


n = int(input("Introducir numero de nodos: "))
o = int(input("Introducir nodo de origen: "))
d = int(input("Introducir nodo de destino: "))
i = 0
j = 0
flujom = 0

graf = []  # Matriz del grafo
rutas = []  # lista de rutas

#  Rellenar la matriz de distancias , distancias asi mismas valen 0 por defecto
for i in range(n):
    graf.append([])
    for j in range(n):
        if i == j:
            dis = 0
            graf[i].append(dis)
        else:
            dis = float(input(f"Indique flujo {i}{j}: "))
            graf[i].append(dis)

for v in range(0, n):
    rutas.append(0)

graf2 = graf
while constructor_rutas(graf, o, d, rutas, n):
    minflu = 9999999
    j = d
    while j != o:
        i = rutas[j] # Construimos las rutas de atras hacia adelante
        minflu = min(minflu, graf2[i][j])
        j = rutas[j]

    j = d
    while j != o:
        i = rutas[j]
        graf2[i][j] = graf2[i][j] - minflu #Actualizar los flujos
        graf2[j][i] = graf2[j][i] + minflu
        j = rutas[j]

    flujom = flujom + minflu

print(f"El flujo maximo es: {flujom}")
