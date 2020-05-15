#No rompe ciclos


import numpy as np
import collections

z = 0
ntrd = int(input("Inserte el número de nodos: "))

a = np.zeros((3, ntrd, ntrd))

size = len(a[0][0,:])

#Relación
for i in range(ntrd):  
    for j in range(ntrd):
        if i == j:
            a[0][i][j]=0
        else:
            a[0][i][j] = int(input(f"Inserte la relación entre E{i+1} y S{j+1}: "  ))

for i in range(ntrd):  
    for j in range(ntrd):
        if i == j:
            a[0][i][j] = a[0].max()+1
        else:
            a[0][i][j] = a[0][i][j]

print()
print(a[0])
#Restar valor minimo en fila
for i in range(ntrd):  
    z = z + a[0][i,:].min()
    a[0][i,:] = a[0][i,:] - min(a[0][i,:])

print()
print(a[0])
#Restar valor minimo el columna
for j in range(ntrd):
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
        print()
        print("Asignación completa")
        print()
        print(a[0])
        print()
        print("Z = ",z)
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

