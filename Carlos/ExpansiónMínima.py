class Graph:
    
    #Determinación de las distancias mínimas
    def minDistance(self,key,mstSet):
        min = float("Inf")
        for v in range(nodes):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
    
    #Impresión del valor óptimo
    def printSolution(self,parent):
        print("\n\tSolución Óptima")
        for i in range(1,nodes):
            #Impresión del camino óptimo por seguir
            print ("\nIr del nodo",parent[i],"hacia el nodo",i,"con costo:\t",self.graph[i][parent[i]])
                       
    #Algoritmo de Prim
    def prim(self, graph, vOrig):
        key = [float("Inf")]*nodes
        parent = [None]*nodes
        key[0]=0
        mstSet = [False]*nodes
        parent[0] = -1
        
        for cout in range(nodes):
            u = self.minDistance(key,mstSet)
            mstSet[u] = True
            for v in range(nodes):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    
        #Llamada a la función de impresión del valor óptimo            
        self.printSolution(parent)
        
g = Graph()

#Inicialización de datos
nodes = int(input("Ingrese el número de nodos en el grafo: "))
vOrig = int(input("Ingrese el nodo de origen: "))
input("Si el costo entre nodos no existe teclear 9999")

g.graph = []  # Matriz de costos

#Asignación de costos entre nodos
for i in range(nodes):
    g.graph.append([])
    for j in range(nodes):
        if (i==j):
            cost = 0
            g.graph[i].append(cost)
        else:
            cost = float(input(f"Indique el costo de ir de {i} a {j}: "))
            g.graph[i].append(cost)

#Llama a la función Dijkstra
g.prim(g.graph, vOrig)