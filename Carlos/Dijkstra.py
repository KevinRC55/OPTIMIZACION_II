class Graph:
    
    #Determinación de las distancias mínimas
    def minDistance(self, dist, queue):
        minimum = float("Inf")
        min_index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
    
    #Impresión del camino óptimo a seguir
    def printPath(self, parent, j):
        if parent[j] == -1:
            print (j),
            return
        self.printPath(parent, parent[j])
        print (j),

    #Impresión del valor óptimo
    def printSolution(self, dist, parent):
        src = 0
        for i in range(1, len(dist)):
            #Impresión del valor óptimo y llamada a la función de camino óptimo
            print("\nEl costo de ir de %d a %d es: %d \nY la ruta por recorrer es la siguiente:" % (src, i, dist[i])),
            self.printPath(parent, i)
            
    #Algoritmo de Dijkstra
    def dijkstra(self, graphCost, vOrig):

        row = len(graphCost)
        col = len(graphCost[0])

        dist = [float("Inf")] * row

        parent = [-1] * row
        
        dist[vOrig] = 0

        queue = []
        for i in range(row):
            queue.append(i)

        while queue:
            #Llamada a la función para determinar distancias mínimas
            u = self.minDistance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if graphCost[u][i] and i in queue:
                    if dist[u] + graphCost[u][i] < dist[i]:
                        dist[i] = dist[u] + graphCost[u][i]
                        parent[i] = u
                        
        #Llamada a la función de impresión del valor óptimo
        self.printSolution(dist, parent)

g = Graph()

#Inicialización de datos
nodes = int(input("Ingrese el número de nodos en el grafo: "))
vOrig = int(input("Ingrese el nodo de origen: "))
input("Si el costo entre nodos no existe teclear 9999")

graphCost = []  # Matriz de costos

#Asignación de costos entre nodos
for i in range(nodes):
    graphCost.append([])
    for j in range(nodes):
        if (i==j):
            cost = 0
            graphCost[i].append(cost)
        else:
            cost = float(input(f"Indique el costo de ir de {i} a {j}: "))
            graphCost[i].append(cost)

#Llama a la función Dijkstra
g.dijkstra(graphCost, vOrig)