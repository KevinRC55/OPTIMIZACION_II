import numpy as np
import collections

z = 0
ntrd = int(input("Inserte el número de nodos de entrada: "))
sld = int(input("Inserte el número de nodos de salida: "))

#Balancear
if ntrd > sld:
    a = np.zeros((4, ntrd, sld+1)) 
elif ntrd < sld:
    a = np.zeros((4, ntrd+1, sld))
else:
    a = np.zeros((4, ntrd, sld))

size = len(a[0][0,:])

#Relación
for i in range(ntrd):  
    for j in range(sld):
        a[0][i][j] = int(input(f"Inserte la relación entre E{i+1} y S{j+1}: "  ))

print()
print(a[0])
a[3] = a[0]
#Restar valor minimo el fila
for i in range(ntrd):  
    z = z + a[0][i,:].min()
    a[0][i,:] = a[0][i,:] - min(a[0][i,:])

print()
print(a[0])
#Restar valor minimo el columna
for j in range(sld):
    z = z + a[0][:,j].min()  
    a[0][:,j] = a[0][:,j] - min(a[0][:,j])

print()
print(a[0])

a[1] = a[0]

cntdr = 0
stop = False

while(cntdr != size):
    #Buscar 0s y tachar renglones o columnas
    while(stop == False):
        i,j = np.where(a[1]==0)
        ii,jj = i[0],j[0]
        #Tachar renglon o columna con mas 0s
        fl = collections.Counter(a[1][ii,:])[0]
        clmn = collections.Counter(a[1][:,jj])[0]

        if(fl > clmn):
            a[1][ii,:] = a[1].max()+1
            a[2][ii,:] = a[2][ii,:]+1
        else: 
            a[1][:,jj] = a[1].max()+1
            a[2][:,jj] = a[2][:,jj]+1

        aux = 0
        for i in range(size):  
            for j in range(size):
                if(a[1][i,j]==0):
                    aux = aux+1
                else:
                    aux = aux

        if(aux>0):
            stop=False
            cntdr = cntdr + 1
        else:
            stop=True
            cntdr = cntdr + 1

    #Comprobar numero de taches = nodos
    if (cntdr == size):
        print("\nAsignación completa\n")
        print(a[0])
        print("\nZ = ",z,"\n")
    else:
        a[0] = np.where(a[2]!=2,a[0],a[0]+a[1].min())
        a[0] = np.where(a[2]!=0,a[0],a[0]-a[1].min())
        z = z + a[1].min()
        print()
        print(a[0])
        a[1] = a[0]
        a[2] = np.where(a[2]!=a[2],a[2],0)
        stop = False
        cntdr = 0

#Resultados
a[1] = a[0]
cntdr = 0
print("\n||Asignacion||\n")
while cntdr != size:
    for i in range(size):  
        for j in range(size):
            if a[1][i,j] == 0:
                fl = collections.Counter(a[1][i,:])[0]
                clmn = collections.Counter(a[1][:,j])[0]
                if fl == 1 or clmn == 1:
                    print("Del nodo ",i+1," al nodo ",j+1," con relacion ",a[3][i,j],"\n")
                    a[1][i,:] = a[1].max()
                    a[1][:,j] = a[1].max()
                    cntdr = cntdr + 1
                else:
                    a[1][i,j] = a[1][i,j]
            else:
                a[1][i,j] = a[1][i,j]
                
