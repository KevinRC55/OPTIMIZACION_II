# Problema de tipo mochila

# Las entradas a usar serán:
# PesoMaximo: peso máximo a cargar
# PesoElemento: peso de cada elemento
# Coeficientes: coeficiente de la funcion objetivo
# n: número de variables

def ProblemaMochila(PesoMaximo, PesoElemento, Coeficientes, n): 
    # Ya que el problema es de maximización, se empieza inicializando
    # las variables en 1, asi se generarán  bloques de 1's y 0's con todas las combinaciones

    Mochila = [[1 for PesoMaximo in range(PesoMaximo + 1)] 
            for i in range(n + 1)] 
              
    for i in range(n + 1): 
        for PesoMaximo in range(PesoMaximo + 1): 
            if i == 0 or PesoMaximo == 0: 
                Mochila[i][PesoMaximo] = 0
            elif PesoElemento[i - 1] <= PesoMaximo: 
                Mochila[i][PesoMaximo] = max(Coeficientes[i - 1]  
                  + Mochila[i - 1][PesoMaximo - PesoElemento[i - 1]], 
                               Mochila[i - 1][PesoMaximo]) 
            else: 
                Mochila[i][PesoMaximo] = Mochila[i - 1][PesoMaximo] 
  
    res = Mochila[n][PesoMaximo] 
    print("Z:",res) 
      
    PesoMaximo = PesoMaximo 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        if res == Mochila[i - 1][PesoMaximo]: 
            continue
        else: 
  
            # Estos Coeficientesores serań incluidos en la mochila 
            print("Estos pesos seran incluidos:",PesoElemento[i - 1]) 
              
            res = res - Coeficientes[i - 1] 
            PesoMaximo = PesoMaximo - PesoElemento[i - 1] 
  

# Llamado a funcion

Coeficientes = [ 10,9,8,8,7,6 ] 
PesoElemento = [ 26,23,21,15,12,8 ] 
PesoMaximo = 70
n = len(Coeficientes) 
      
ProblemaMochila(PesoMaximo, PesoElemento, Coeficientes, n) 
  
