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

C = float(input('Ingresa el peso máximo:'))
Pesos = [26,23,21,15,12,8]
Valores = [10,9,8,8,7,6]
n = len(Valores)

Z =  ProblemaMochila(n,C,Valores,Pesos)
print("Z:",Z)


'''
En el siguiente árbol de recursión, M () se refiere 
ProblemaMochila (). Los dos parámetros indicados en el
Los siguientes árboles de recursión son n y  C.
El árbol de recursión es para las siguientes entradas de muestra.
Pesos [] = {1, 1, 1}, C = 2, Valores [] = {10, 20, 30}
                       M (n, C)
                        (3, 2)  
                   / \ 
                 / \               
            M (2, 2) M (2, 1)
          / \ / \ 
        / \ / \
       M (1, 2) M (1, 1) M (1, 1) M (1, 0)
       / \ / \ / \
     / \ / \ / \
M (0, 2) M (0, 1) M(0, 1) M(0, 0) M(0, 1) M(0, 0)
Árbol de recursión
'''

