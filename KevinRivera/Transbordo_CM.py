#Solo asignacion por costo minimo

#a[0] = Matriz de asignación
#a[1] = Matriz de costos
#a[2] = Auxiliar/Matriz de presios sombra
#a[3] = Matriz identificadora de asignación
#a[4] = Auxiliar
import numpy as np

frt = int(input("Inserte el numero de nodos de oferta: "))
dmnd = int(input("Inserte el numero de nodos de demanda: "))
trnsbrd = int(input("Inserte el numero de nodos de transbordo: "))
print()
frtt = frt + trnsbrd
dmndt = dmnd + trnsbrd
ot = np.zeros((frtt, 1))
dt = np.zeros((1,dmndt))
ott = 0
dtt = 0
tt = 0 #Suma de transbordos
#Ofertas y demandas
for i in range(frt):
    ot[i][0] = int(input(f"Inserte la oferta total de O{i+1}: "  ))
    ott = ott + ot[i][0] 
for i in range(frtt):
    if ot[i][0] == 0:
        ot[i][0] = ott
        tt = tt + ot[i][0]
    else:
        ot[i][0] = ot[i][0]
print()
for j in range(dmnd):
    dt[0][j] = int(input(f"Inserte la demanda total de D{j+1}: "  ))
    dtt = dtt + dt[0][j]
for j in range(dmndt):
    if dt[0][j] == 0:
        dt[0][j] = ott
    else:
        dt[0][j] = dt[0][j]
print()

#Demanda u oferta artificial
if ott > dtt:
    a = np.zeros((5, frtt, dmndt+1))
    dfrnc = np.array([[(ott+tt) - (dtt+tt)]])
    dt = np.append(dt, dfrnc, axis=1)
elif ott < dtt:
    a = np.zeros((5, frtt+1, dmndt))
    dfrnc = np.array([[(dtt+tt) - (ott+tt)]])
    ot = np.append(ot, dfrnc, axis=0)
else:
    a = np.zeros((5, frt, dmnd))

oi = ott
di = dtt
ott = ott + tt
dtt = dtt + tt

sizeof = len(a[0][:,0])
sizede = len(a[0][0,:])

#Costos
to = frt#Indice de transbordos
td = dmnd#Indice de transbordos
for i in range(frtt):  
    for j in range(dmndt):
        if i >= to and j >= td:
            a[1][i][j] = int(input(f"Inserte el costo de T a T: "  ))
        elif i >= to:
            a[1][i][j] = int(input(f"Inserte el costo de T a D{j+1}: "  ))
        elif j >= td:
            a[1][i][j] = int(input(f"Inserte el costo de O{i+1} a T: "  ))
        else:    
            a[1][i][j] = int(input(f"Inserte el costo de O{i+1} a D{j+1}: "  ))
        
a[4] = a[1]

#Restringir asignacion de transbordos a transbordos
for i in range(sizeof):  
    for j in range(sizede):
        if i >= to and j >= td:
            a[1][i][j] = a[1].max()+1
        else:
            a[1][i][j] = a[1][i][j]

a[1] = np.where(a[1]!=0,a[1],2*a[1].max())
usar = dtt-(oi+di)

#Asignar costo minimo
print("\nCosto Mínimo: \n")
while dtt != 0:
    if dtt == usar:
         for i in range(frtt):  
            for j in range(dmndt):
                if i >= to and j >= td:
                    a[1][i][j] = a[4][i][j]
                else:
                    a[1][i][j] = a[1][i][j]
    #Identificar costo minimo
    i,j = np.where(a[1]==a[1].min())
    ii,jj = i[0],j[0]

    #Agotar demandas
    if (ot[ii][0] > dt[0][jj]):
        a[0][ii][jj] = dt[0][jj]
        a[3][ii][jj] = 1
        ot[ii][0] = ot[ii][0] - dt[0][jj]
        ott = ott - dt[0][jj]
        dtt = dtt - dt[0][jj]
        dt[0][jj] = dt[0][jj] - a[0][ii][jj]
        a[1][:,jj] =  a[1].max()+1
    else:
        a[0][ii][jj] = ot[ii][0]
        a[3][ii][jj] = 1
        dt[0][jj] = dt[0][jj] - a[0][ii][jj]
        ott = ott - ot[ii][0]
        dtt = dtt - ot[ii][0]
        ot[ii][0] = ot[ii][0] - a[0][ii][jj]
        a[1][ii,:] =  a[1].max()+1
    print(a[0],"\n")

#Llenar la ultima columna
if(ott > dtt):
    a[0][:,dmndt] = ot[:,0]
    a[3][:,dmndt] = np.where(a[0][:,dmndt]==0,a[3][:,dmndt],1)
elif(ott < dtt):
    a[0][frtt,:] = dt[0,:]
    a[3][frtt,:] = np.where(a[0][frtt,:]==0,a[3][frtt,:],1)
else:
    a[0] = a[0]
    a[3] = a[3]

#Función objetivo
a[1] = a[4]
z=0
for i in range(sizeof):  
    for j in range(sizede):
        z = z + a[0][i,j]*a[1][i,j]

print("Z= ",z,"\n")

