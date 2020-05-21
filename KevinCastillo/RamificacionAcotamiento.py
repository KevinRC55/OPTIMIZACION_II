#tenemos las siguientes entradas:
#Pesos
#Valores
#n: representa la longitud del vector valores
#C: representa el peso máximo a cargar

#Este problema se resolvera usando programación dinamica
# como primer paso damos una solución recursiva

#n representa la posicion del puntero
def ProblemaMochila(n,C,Valores,Pesos):
    #Iniciamos con el caso base
    if n == 0 or C == 0:
        return 0
    #Inicializamos al puntero en la última posición
    elif Pesos[n-1] > C:
        # En caso de que el peso de la n-sima posicion sea mayor
        # que  el costo máximo, recorreremos una posicion al puntero
        print('No se incluye en la solucion optima')
        return(ProblemaMochila(n-1,C,Valores,Pesos))
    else:
        #En caso de no meterlo a la bolsa
        Decision1 = ProblemaMochila(n-1,C,Valores,Pesos)
        #En caso de meterlo a la bolsa
        Decision2 = Valores[n-1] + ProblemaMochila(n-1,C-Pesos[n-1],Valores,Pesos)
        print(Decision1,Decision2)
        Resultado = max(Decision1,Decision2)
        
        
        return(Resultado)



# Llamado a la funcion ProblemaMochila

C = 70
Pesos = [26,23,21,15,12,8]
Valores = [10,9,8,8,7,6]
n = len(Valores)

Z =  ProblemaMochila(n,C,Valores,Pesos)
print("Z:",Z)


'''
En el siguiente árbol de recursión, K () se refiere 
knapSack (). Los dos parámetros indicados en el
Los siguientes árboles de recursión son ny W.
El árbol de recursión es para las siguientes entradas de muestra.
wt [] = {1, 1, 1}, W = 2, val [] = {10, 20, 30}
                       K (n, W)
                       K (3, 2)  
                   / \ 
                 / \               
            K (2, 2) K (2, 1)
          / \ / \ 
        / \ / \
       K (1, 2) K (1, 1) K (1, 1) K (1, 0)
       / \ / \ / \
     / \ / \ / \
K (0, 2) K (0, 1) K (0, 1) K (0, 0) K (0, 1) K (0, 0)
Árbol de recursión para mochila Capacidad 2 
unidades y 3 artículos de 1 unidad de peso.
'''

