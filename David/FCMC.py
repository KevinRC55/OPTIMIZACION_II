import numpy as np

N=int(input("Cantidad total de nodos:       "))
l=int(input("Cantidad total de conexiones:  "))
Nodos=np.zeros((l,5))
O_D=np.zeros((N,1))
forzados=0
index=0
B=0
a=0

"Ofertas y demandas"
for i in range(N):
    O_D[i]=int(input(f"Oferta/Demanda del nodo {i+1}:       "))

"Conexiones"
while(index!=l):
    print(f"Conexión {index+1}")
    Nodos[index,0]=int(input("Nodo origen:      "))-1
    Nodos[index,1]=int(input("Nodo destino:     "))-1
    Nodos[index,2]=int(input("Flujo Mínimo:     "))
    if(Nodos[index,2]>0):
        forzados+=1
    Nodos[index,3]=int(input("Flujo Máximo:      "))
    Nodos[index,4]=int(input("Costo por unidad:  "))
    index+=1

print(Nodos)

"Solución inicial dirigida a balancear"
for i in range(N):
    B=B+O_D[i]
if(B!=0):
    "Se agrega Nodo de balance y artificial"
    Solucion=np.zeros((N+forzados+1,3))
    a=1
else:
    Solucion=np.zeros((N+forzados,3))

for i in range(N):
    if(O_D[i]>0):
        Solucion[i,0]=i
        Solucion[i,1]=10
        Solucion[i,2]=O_D[i]
    elif(O_D[i]<0):
        Solucion[i,0]=10
        Solucion[i,1]=i
        Solucion[i,2]=abs(O_D[i])
print(Solucion)

Fin=0
while(Fin<2):
    costo=0
    ori=0
    de=0
    "W y Precios Sombra"
    W=np.zeros((N+1+a,1))
    PSombras=np.zeros((l,1))

    for i in range(N):
        if(Solucion[i,0]==10 or Solucion[i,1]==10):
            if(Solucion[i,0]==10):
                W[i]=-100
            else:
                W[i]=100
    for i in range(N):
        if(W[i]==0):
            for j in range(l):
                if(Nodos[j,0]==Solucion[i,0] and Nodos[j,1]==Solucion[i,1]):
                    ori=int(Solucion[i,0])
                    de=int(Solucion[i,1])
                    if(W[ori]!=0):
                        W[i]=W[ori]-Nodos[j,4]
                    else:
                        W[i]=W[de]+Nodos[j,4]

    print("Valores W")
    print(W)

    o=0
    d=0
    o0=0
    d0=0
    f=0
    for i in range(l):
        o=int(Nodos[i,0])
        d=int(Nodos[i,1])
        PSombras[i]=W[o]-W[d]-Nodos[i,4]

    print("Precios Sombra")
    print(PSombras)

    P=max(PSombras)
    "Comprobación de precios sombra>0"
    if(P<=0):
        Fin=1
    else:
        for i in range(l):
            if P==PSombras[i]:
                o=int(Nodos[i,0])
                d=int(Nodos[i,1])
    o0=o
    d0=d
    of=0
    df=0
    Final=o
    piv=np.zeros((l,3))
    itr=0
    Ciclo=0
    num=0
    F=0
    p=0
    R=0
    "Pivoteo"
    while(p<4):
        k=0
        m=0
        if(itr==0):
            piv[0,0]=o
            piv[0,1]=d
            for i in range(N):
                if(Solucion[i,0]==d): 
                    o=Solucion[i,0]
                    d=Solucion[i,1]
                    piv[itr+1,2]=1
                    itr+=1
                elif(Solucion[i,1]==d):
                    o=Solucion[i,0]
                    d=Solucion[i,1]
                    piv[itr+1,2]=-1
                    itr+=1
        if(itr>0):
            piv[itr,0]=o
            piv[itr,1]=d
            if(F!=1):
                for i in range(N):
                    if(Solucion[i,0]==Final):
                        o=Solucion[i,0]
                        d=Solucion[i,1]
                        piv[itr+1,2]=-1
                        F=1
                        itr+=1
                        print(o,d)
                        break
                    elif(Solucion[i,1]==Final):
                        o=Solucion[i,0]
                        d=Solucion[i,1]
                        piv[itr+1,2]=1
                        F=1
                        itr+=1
                        print(o,d)
                        break
            for i in range(N):
                if(Solucion[i,0]==d):
                    o=Solucion[i,0]
                    d=Solucion[i,1]
                    piv[itr+1,2]=1
                    itr+=1
                    break
                elif(Solucion[i,1]==d):
                    if(Solucion[i,0]==o):
                        d=o
                    else:
                        o=Solucion[i,0]
                        d=Solucion[i,1]
                        piv[itr+1,2]=-1
                        itr+=1
                        break
        print("Pivoteo del paso")
        print(piv)
        p+=1
    k=0
    print("Pivoteo encontrado")
    print(piv)

    for i in range(N-1):
        if(piv[i,0]==piv[i,1]):
            piv[i,0]=piv[i+1,0]
            piv[i,1]=piv[i+1,0]
    
    print("Pivoteo")
    print(piv)

    for i in range(l-2):
        if(piv[i,0]==piv[i+1,0] and piv[i,1]==piv[i+1,1]):
            piv[i+1,0]=piv[i+2,0]
            piv[i+1,1]=piv[i+2,1]
            piv[i+1,2]=piv[i+2,2]
    print("Quitando repetidos")
    for i in range(l-2):
        if(piv[i,0]==piv[i,1]):
            piv[i,0]=piv[i+1,0]
            piv[i,1]=piv[i+1,1]
            piv[i+1,0]=0
            piv[i+1,1]=0
    print(piv)
    

    print("Pivoteo")
    print(piv)

    "Cálculo de la menor delta"
    delta=100
    for i in range(l):
        if(piv[0,0]==Nodos[i,0] and piv[0,1]==Nodos[i,1]):
            delta=Nodos[i,3]
    itr=1
    while(piv[itr,0]!=0 or piv[itr,1]!=0):
        for i in range(N):
            if(piv[itr,0]==Solucion[i,0] and piv[itr,1]==Solucion[i,1]):
                if(Solucion[i,2]<delta):
                    delta=Solucion[i,2]
        itr+=1

    "Cambio en la solución"
    itr=0
    print(piv[itr,0],piv[itr,1])
    while(piv[itr,0]!=0 or piv[itr,1]!=0): 
        for i in range(N):    
            if(piv[itr,0]==Solucion[i,0] and piv[itr,1]==Solucion[i,1]):
                Solucion[i,2]+=delta*piv[itr,2]
                """if(piv[itr,2]==0 and piv[itr,0]!=o0 and piv[itr,1]!=d0):
                    Solucion[i,2]+=delta"""
        itr+=1
    print(delta)
    print(Solucion)
    for i in range(N):
        if(Solucion[i,2]==0):
            Solucion[i,0]=o0
            Solucion[i,1]=d0
            Solucion[i,2]=delta
    print("Nueva Solucion")
    print(Solucion)
    Fin=Fin+1

Z=0
for i in range(N):
    for j in range(l):
        if(Solucion[i,0]==Nodos[j,0] and Solucion[i,1]==Nodos[j,1]):
            Z+=Nodos[j,4]*Solucion[i,2]
print(f"El costo total es: {Z}")