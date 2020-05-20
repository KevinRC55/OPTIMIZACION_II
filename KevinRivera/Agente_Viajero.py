import numpy as np
import collections

def hungaro(mtrz,n):
    b = np.zeros((4, n, n))
    b[0] = mtrz
    b[3] = b[0]
    z = 0
    #Restar valor minimo en fila
    for i in range(n):  
        z = z + b[0][i,:].min()
        b[0][i,:] = b[0][i,:] - min(b[0][i,:])

    print()
    print(b[0])
    #Restar valor minimo el columna
    for j in range(ntrd):
        z = z + b[0][:,j].min()  
        b[0][:,j] = b[0][:,j] - min(b[0][:,j])

    print()
    print(b[0])

    b[1] = b[0]

    cntdr = 0
    stop = False

    while(cntdr != n):
        #Buscar 0s y tachar renglones o columnas
        while(stop == False):
            i,j = np.where(b[1]==0)
            ii,jj = i[0],j[0]
            #Tachar renglon o columna con mas 0s
            fl = collections.Counter(b[1][ii,:])[0]
            clmn = collections.Counter(b[1][:,jj])[0]

            if(fl > clmn):
                b[1][ii,:] = b[1].max()+1
                b[2][ii,:] = b[2][ii,:]+1
            else: 
                b[1][:,jj] = b[1].max()+1
                b[2][:,jj] = b[2][:,jj]+1

            aux = 0
            for i in range(size):  
                for j in range(size):
                    if(b[1][i,j]==0):
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
        if (cntdr == n):
            print()
            print("Asignación completa")
            print()
            print(b[0])
            print()
            print("Z = ",z)
        else:
            b[0] = np.where(b[2]!=2,b[0],b[0]+b[1].min())
            b[0] = np.where(b[2]!=0,b[0],b[0]-b[1].min())
            z = z + b[1].min()
            print()
            print(b[0])
            b[1] = b[0]
            b[2] = np.where(b[2]!=b[2],b[2],0)
            stop = False
            cntdr = 0


def matriz_final(mtrz,n):
    b = np.zeros((4, n, n))
    b[0] = mtrz
    b[3] = b[0]
    z = 0
    #Restar valor minimo en fila
    for i in range(n):  
        z = z + b[0][i,:].min()
        b[0][i,:] = b[0][i,:] - min(b[0][i,:])

    #Restar valor minimo el columna
    for j in range(ntrd):
        z = z + b[0][:,j].min()  
        b[0][:,j] = b[0][:,j] - min(b[0][:,j])

    b[1] = b[0]

    cntdr = 0
    stop = False

    while(cntdr != n):
        #Buscar 0s y tachar renglones o columnas
        while(stop == False):
            i,j = np.where(b[1]==0)
            ii,jj = i[0],j[0]
            #Tachar renglon o columna con mas 0s
            fl = collections.Counter(b[1][ii,:])[0]
            clmn = collections.Counter(b[1][:,jj])[0]

            if(fl > clmn):
                b[1][ii,:] = b[1].max()+1
                b[2][ii,:] = b[2][ii,:]+1
            else: 
                b[1][:,jj] = b[1].max()+1
                b[2][:,jj] = b[2][:,jj]+1

            aux = 0
            for i in range(size):  
                for j in range(size):
                    if(b[1][i,j]==0):
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
        if (cntdr == n):
            b[0] = b[0]
        else:
            b[0] = np.where(b[2]!=2,b[0],b[0]+b[1].min())
            b[0] = np.where(b[2]!=0,b[0],b[0]-b[1].min())
            z = z + b[1].min()
            b[1] = b[0]
            b[2] = np.where(b[2]!=b[2],b[2],0)
            stop = False
            cntdr = 0
    return(b[0])


ntrd = int(input("Inserte el número de nodos: "))

a = np.zeros((4, ntrd, ntrd))

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
            a[0][i][j] = a[0].max()+10
        else:
            a[0][i][j] = a[0][i][j]

print()
print(a[0])

hungaro(a[0],size)

#Resultados
a[1] = matriz_final(a[0],size)
ccl = []
cntdr = 0
print("\n||Asignacion||\n")
while cntdr != size:
    for i in range(size):  
        for j in range(size):
            if a[1][i,j] == 0:
                fl = collections.Counter(a[1][i,:])[0]
                clmn = collections.Counter(a[1][:,j])[0]
                if fl == 1 or clmn == 1:
                    print("Del nodo ",i+1," al nodo ",j+1," con relacion ",a[0][i,j],"\n")
                    a[1][i,:] = a[1].max()
                    a[1][:,j] = a[1].max()
                    ccl.append([i,j])#Nodos en el ciclo
                    cntdr = cntdr + 1
                else:
                    a[1][i,j] = a[1][i,j]
            else:
                a[1][i,j] = a[1][i,j]

#Buscar miniciclos
size = len(ccl)
mccl = False
for k in range(size):
    for l in range(size):
        if ccl[k][0] == ccl[l][1] and ccl[k][1] == ccl[l][0]:
            print("Existe un miniciclo del nodo ",ccl[k][0]+1," al nodo ",ccl[l][0]+1,"\n")
            j = ccl[k][0]
            i = ccl[l][0]
            mccl = True

if mccl == False :
    print("No existen miniciclos\n")
else: 
    print("\nSe rompe el ciclo: nodo ",i+1," al nodo ",j+1,"\n")

    a[2] = a[0]
    a[2][i,j] = a[2].max()+10
    print(a[2])
    hungaro(a[2], size)

    print("\nSe rompe el ciclo: nodo ",j+1," al nodo ",i+1,"\n")

    a[2] = a[0]
    a[2][j,i] = a[2].max()+10
    print(a[2])
    hungaro(a[2], size)
