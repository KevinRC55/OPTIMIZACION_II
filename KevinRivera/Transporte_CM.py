#No funciona si en el pivoteo el ciclo es de mas de 4

#a[0] = Matriz de asignación
#a[1] = Matriz de costos
#a[2] = Auxiliar/Matriz de presios sombra
#a[3] = Matriz identificadora de asignación
#a[4] = Auxiliar
import numpy as np

frt = int(input("Inserte el numero de nodos de oferta: "))
dmnd = int(input("Inserte el numero de nodos de demanda: "))
print()
ot = np.zeros((frt, 1))
dt = np.zeros((1,dmnd))
ott = 0
dtt = 0
#Ofertas y demandas
for i in range(frt):
    ot[i][0] = int(input(f"Inserte la oferta total de O{i+1}: "  ))
    ott = ott + ot[i][0] 
print()
for j in range(dmnd):
    dt[0][j] = int(input(f"Inserte la demanda total de D{j+1}: "  ))
    dtt = dtt + dt[0][j]

#Demanda artificial
if ott > dtt:
    a = np.zeros((5, frt, dmnd+1))
    dfrnc = np.array([[ott - dtt]])
    dt = np.append(dt, dfrnc, axis=1)
elif ott < dtt:
    a = np.zeros((5, frt+1, dmnd))
    dfrnc = np.array([[dtt - ott]])
    ot = np.append(ot, dfrnc, axis=0)
else:
    a = np.zeros((5, frt, dmnd))

sizeof = len(a[0][:,0])
sizede = len(a[0][0,:])
print()
#Costos
for i in range(frt):  
    for j in range(dmnd):
        a[1][i][j] = int(input(f"Inserte el costo de O{i+1} a D{j+1}: "  ))
        
a[4] = a[1]

a[1] = np.where(a[1]!=0,a[1],a[1].max()+1)

print("\nCosto Mínimo: \n")

while dtt != 0:
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
    a[0][:,dmnd] = ot[:,0]
    a[3][:,dmnd] = np.where(a[0][:,dmnd]==0,a[3][:,dmnd],1)
elif(ott < dtt):
    a[0][frt,:] = dt[0,:]
    a[3][frt,:] = np.where(a[0][frt,:]==0,a[3][frt,:],1)
else:
    a[0] = a[0]
    a[3] = a[3]

#Función objetivo
a[1] = a[4]
z=0
for i in range(sizeof):  
    for j in range(sizede):
        z = z + a[0][i,j]*a[1][i,j]


a[2] = a[3]

stop = False

while(stop == False):

    a[2] = a[3]

    #Vectores u y v
    u = np.zeros((frt, 1))
    v = np.zeros((1,sizede))
    ax1 = np.zeros((frt, 1))
    ax2 = np.zeros((1,sizede))
    ax1[0,0] = 1
    cntdr = 0

    while (cntdr != 2):
        while (ax1[:,0].any() > 0):
            i,j = np.where(ax1==ax1.max())
            ii,jj = i[0],j[0]
            while (a[3][ii,:].any() > 0):
                l = np.where(a[3][ii,:]>0)
                ll = l[0][0]
                v[0,ll] = a[1][ii][ll] - u[ii,0]
                ax2[0,ll] = 1
                a[3][ii,ll] = 0 
            ax1[ii,0] = 0
        if(ax2.all() == 1):
            cntdr = cntdr + 1
        else:
            cntdr = cntdr

        a[3] = a[2]

        while (ax2[0,:].any() > 0):
            i,j = np.where(ax2==ax2.max())
            ii,jj = i[0],j[0]
            while (a[3][:,jj].any() > 0):
                k = np.where(a[3][:,jj] > 0)
                kk = k[0][0]
                u[kk,0] = a[1][kk][jj] - v[0,jj]
                ax1[kk,0] = 1
                a[3][kk,jj] = 0
            ax2[0,jj] = 0
        if(ax1.all() == 1):
            cntdr = cntdr + 1
        else:
            cntdr = cntdr

    a[3] = a[2]    

    #Precios sombra
    for i in range(sizeof):  
        for j in range(sizede):
            a[2][i,j] = v[0,j]+u[i,0]-a[1][i,j]

    print("\nAsignación")
    print(a[0])
    print("\nPrecios sombra")
    print(a[2])
    print("\nu")
    print(u)
    print("\nv")
    print(v)
    print("\nZ =",z,"\n")
    
    #Determinar precios sombra <= 0 
    cntdr = 0
    for i in range(sizeof):  
        for j in range(sizede):
            if(a[2][i,j]>0):
                cntdr = cntdr+1
            else:
                cntdr = cntdr

    if(cntdr>0):
        stop=False
    else:
        stop=True


    if (stop == True):
        print("¡La solución es optima!\n")
    else:
        #Buscar otra solución factible
        #Posición de precio sombra mayor
        i,j = np.where(a[2]==a[2].max())
        ii,jj = i[0],j[0]
        sm = a[2].max()

        ccl = []
        cclp = [[ii,jj]]

        #Buscar ciclo
        k = np.where(a[3][:,jj] > 0)
        kk = k[0][0]
        ccl.append(a[0][kk,jj])
        cclp.append([kk,jj])
        l = np.where(a[3][ii,:] > 0)
        ll = l[0][0]
        ccl.append(a[0][ii,ll])
        cclp.append([ii,ll])

        ccl.append(a[0][kk,ll])
        cclp.append([kk,ll])

        #pivoteo
        i = np.where(ccl==min(ccl))
        ii = i[0][0]
        i,j = cclp[ii+1]
        a[3][i,j] = 0

        i,j = cclp[0]
        a[0][i,j] = a[0][i,j] + min(ccl)
        a[3][i,j] = 1
        i,j = cclp[1]
        a[0][i,j] = a[0][i,j] - min(ccl)
        i,j = cclp[2]
        a[0][i,j] = a[0][i,j] - min(ccl)
        i,j = cclp[3]
        a[0][i,j] = a[0][i,j] + min(ccl)

        z=0
        for i in range(sizeof):  
            for j in range(sizede):
                z = z + a[0][i,j]*a[1][i,j]
