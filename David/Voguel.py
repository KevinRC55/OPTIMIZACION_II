import numpy as np

"Ofertas y demandas"
x=int(input("Cantidad de puntos de oferta       "))
y=int(input("Cantidad de puntos de demanda      "))
ofert=np.zeros((x,1))
demt=np.zeros((1,y))

j=0
ot=0
dt=0

for k in range(x):
    ofert[k,0]=int(input(f"Ingrese la oferta de O{k+1}:     "))
    ot=ot+ofert[k,0]

for k in range(y):
    demt[0,k]=int(input(f"Ingrese la demanda de D{k+1}:     "))
    dt=dt+demt[0,k]

"Generación de matriz"
ofer=x+j
dem=y+j
C=0
F=0
if ot>dt:
    Costos=np.zeros((ofer,dem+1))
    Valores=np.zeros((ofer,dem+1))
    PSombras=np.zeros((ofer,dem+1))
    for k in range(x):
        for l in range(y):
            Costos[k,l]=int(input(f"Ingrese el costo de O{k+1} a D{l+1}:    "))
    dif=ot-dt
    C=1
elif dt>ot:
    Costos=np.zeros((ofer+1,dem))
    Valores=np.zeros((ofer+1,dem))
    PSombras=np.zeros((ofer+1,dem))
    for k in range(x):
        for l in range(y):
            Costos[k,l]=int(input(f"Ingrese el costo de O{k+1} a D{l+1}:    "))
    dif=dt-ot
    F=1
elif dt==ot:
    Costos=np.zeros((ofer,dem))
    Valores=np.zeros((ofer,dem))
    PSombras=np.zeros((ofer,dem))
    for k in range(x):
        for l in range(y):
            Costos[k,l]=int(input(f"Ingrese el costo de O{k+1} a D{l+1}:    "))

index=0
CCostos=Costos.copy()
while(index<(x*y)):
    minf2=np.zeros((x,1))
    minf1=np.zeros((x,1))
    minv1=np.zeros((y,1))
    minv2=np.zeros((y,1))
    x_f=np.zeros((x,1))
    y_f=np.zeros((x,1))
    x_c=np.zeros((y,1))
    y_c=np.zeros((y,1))
    c=0

    "Mínimos por fila"
    for i in range(x):
        minf1[i]=min(CCostos[i,0:y])
        minf2[i]=10000

    for i in range(x):
        for j in range(y):
            if(CCostos[i,j]==minf1[i]):
                x_f[c]=i
                y_f[c]=j
        c=c+1

    for i in range(x):
        for j in range(y):
            if(i!=x_f[i] or j!=y_f[i]):
                if(CCostos[i,j]<minf2[i]):
                    minf2[i]=CCostos[i,j]

    "Mínimo por columna"
    for j in range(y):
        minv1[j]=min(CCostos[0:x,j])
        minv2[j]=10000

    c=0
    for j in range(y):
        for i in range(x):
            if(CCostos[i,j]==minv1[j]):
                x_c[c]=i
                y_c[c]=j
        c=c+1

    for j in range(y):
        for i in range(x):
            if(i!=x_c[j] or j!=y_c[j]):
                if(CCostos[i,j]<minv2[j]):
                    minv2[j]=CCostos[i,j]      

    "Restas por filas y columnas"
    RestasF=np.zeros((x,1))
    RestasC=np.zeros((y,1))

    for i in range(x):
        RestasF[i]=minf2[i]-minf1[i]
    for j in range(y):
        RestasC[j]=minv2[j]-minv1[j]

    "Asignación de valores"
    xmax=10
    ymax=10
    Vmax=max(max(RestasF),max(RestasC))
    for i in range(x):
        if(RestasF[i]==Vmax):
            xmax=i
    for j in range(y):
        if(RestasC[j]==Vmax):
            ymax=j

    cmax=100000
    if(xmax!=10):
        for j in range(y):
            if(CCostos[xmax,j]<cmax):
                cmax=CCostos[xmax,j]
                ymax=j
        CCostos[xmax,ymax]=1000
        valor=min(ofert[xmax,0],demt[0,ymax])
        Valores[xmax,ymax]=valor
        ofert[xmax,0]=ofert[xmax,0]-Valores[xmax,ymax]
        demt[0,ymax]=demt[0,ymax]-Valores[xmax,ymax]
    elif(ymax!=10):
        for i in range(x):
            if(CCostos[i,ymax]<cmax):
                cmax=CCostos[i,ymax]
                xmax=i     
        CCostos[xmax,ymax]=1000
        valor=min(ofert[xmax,0],demt[0,ymax])
        Valores[xmax,ymax]=valor
        ofert[xmax,0]=ofert[xmax,0]-Valores[xmax,ymax]
        demt[0,ymax]=demt[0,ymax]-Valores[xmax,ymax]

    index=index+1

if(C==1):
    for i in range(x):
        Valores[i,y]=ofert[i,0]
if(F==1):
    for j in range(y):
        Valores[x,j]=demt[0,j]

print("Solución Inicial")
print(Valores)

Optimo=0

while(Optimo!=1):
    u=[None]*len(Costos)
    v=[None]*len(Costos[0])
    u[0]=0

    "Cálculo de vectores para Precios Sombra"
    if(C==1):
        for i in range(x):
            for j in range(y+1):
                if u[i] is None and v[j] is None:
                    continue
                if u[i] is None and Valores[i,j]!=0:
                    u[i]=Costos[i,j]-v[j]
                elif v[j] is None and Valores[i,j]!=0:
                    v[j]=Costos[i,j]-u[i]
        for i in range(x):
            for j in range(y+1):
                if u[i] is None and v[j] is None:
                    continue
                if u[i] is None and Valores[i,j]!=0:
                    u[i]=Costos[i,j]-v[j]
                elif v[j] is None and Valores[i,j]!=0:
                    v[j]=Costos[i,j]-u[i]
        for i in range(x):
            for j in range(y+1):
                PSombras[i,j]=u[i]+v[j]-Costos[i,j]
    elif(F==1):
        for i in range(x+1):
            for j in range(y):
                if u[i] is None and v[j] is None:
                    continue
                if u[i] is None and Valores[i,j]!=0:
                    u[i]=Costos[i,j]-v[j]
                    print(u[i])
                elif v[j] is None and Valores[i,j!=0]:
                    v[j]=Costos[i,j]-u[i]
                    print(v[j])
        for i in range(x+1):
            for j in range(y):
                if u[i] is None and v[j] is None:
                    continue
                if u[i] is None and Valores[i,j]!=0:
                    u[i]=Costos[i,j]-v[j]
                    print(u[i])
                elif v[j] is None and Valores[i,j!=0]:
                    v[j]=Costos[i,j]-u[i]
                    print(v[j])
        for i in range(x+1):
            for j in range(y):
                PSombras[i,j]=u[i]+v[j]-Costos[i,j]
    else:
        for i in range(x):
            for j in range(y):
                if u[i] is None and v[j] is None:
                    continue
                if u[i] is None and Valores[i,j]!=0:
                    u[i]=Costos[i,j]-v[j]
                elif v[j] is None and Valores[i,j]!=0:
                    v[j]=Costos[i,j]-u[i]
        for i in range(x):
            for j in range(y):
                if u[i] is None and v[j] is None:
                    continue
                if u[i] is None and Valores[i,j]!=0:
                    u[i]=Costos[i,j]-v[j]
                elif v[j] is None and Valores[i,j]!=0:
                    v[j]=Costos[i,j]-u[i]
        for i in range(x):
            for j in range(y):
                PSombras[i,j]=u[i]+v[j]-Costos[i,j]

    "Pivoteo"
    P=-500
    for i in range(x):
        for j in range(y):
            if(PSombras[i,j]>P):
                P=PSombras[i,j]
    Px1=0
    Py1=0
    Px2=0
    Py2=0
    Piv=0
    Nv=0
    Z=0

    if(P>0):
        print("La solución no es óptima.")
        for i in range(x):
            for j in range(y+1):
                if(PSombras[i,j]==P):
                    Px1=i
                    Py1=j
                    Px2=i

        for j in range(y+1):
            if (Valores[Px1,j]!=0 and j!=Py1):
                Py2=j
                for i in range(x):
                    if i!=Px1:
                        if (Valores[i,Py1]!=0 and Valores[i,Py2]!=0):
                                Nv=min(Valores[Px2,Py2],Valores[i,Py1])
                                Valores[Px1,Py1]=Nv
                                Valores[Px2,Py2]=Valores[Px2,Py2]-Nv
                                Valores[i,Py1]=Valores[i,Py1]-Nv
                                Valores[i,Py2]=Valores[i,Py2]+Nv
        print("Nueva solución")
        print(Valores)
                        
    else:
        print("La solución es Óptima")
        for i in range(x):
            for j in range(y):
                Z+=Costos[i,j]*Valores[i,j]
        print(f"El costo total es {Z}")    
        Optimo=1