print("************MENÚ PRINCIPAL**************")

Decision = input("""
                    A: Transporte
                    B: Transbordo
                    C: Asignación
                    D: Redes
                    E: Programación entera

                    Elija una opción: """)

if Decision == "A" or Decision =="a":
    print("Selecciona el método de Transporte  a implementar:")
    AlgoritmoTransporte = input("""
                                    A: Esquina Noroeste
                                    B: Costo Mínimo
                                    C: Voguel

                                    Elija una opción: """)
    if AlgoritmoTransporte == "A" or AlgoritmoTransporte == "a":
        Archivo1 = open("TransporteEsquinaNoroeste.py")
        exec(Archivo1.read())
    
    elif AlgoritmoTransporte == "B" or AlgoritmoTransporte == "b":
        Archivo2 = open("TransporteCostoMinimo.py")
        exec(Archivo2.read())
    
    elif AlgoritmoTransporte == "C" or AlgoritmoTransporte == "c":
        Archivo3 = open("TransporteVogel.py")
        exec(Archivo3.read())


elif Decision == "B" or Decision =="b":
    print("Selecciona el método de Transbordo  a implementar:")
    AlgoritmoTransbordo = input("""
                                    A: Esquina Noroeste
                                    B: Costo Minimo
                                    C: Voguel

                                    Elija una opción: """)
    if AlgoritmoTransbordo == "A" or AlgoritmoTransbordo == "a":
        Archivo4 = open("TransbordoEsquinaNoroeste.py")
        exec(Archivo4.read())
    
    elif AlgoritmoTransbordo == "B" or AlgoritmoTransbordo == "b":
        Archivo5 = open("TransbordoCostoMinimo.py")
        exec(Archivo5.read())
   
    elif AlgoritmoTransbordo == "C" or AlgoritmoTransbordo == "c":
       Archivo6 = open("TransbordoVoguel.py")
       exec(Archivo6.read())

elif Decision == "C" or Decision =="c":
    print("Método Hungaro")
    Archivo7 = open("Hungaro.py")
    exec(Archivo7.read())

elif Decision =="D" or Decision =="d":
    print("Selecciona el algoritmo de Redes a implementar:")
    AlgoritmoRedes = input(""" 
                             A: Arbol de expansión mínima
                             B: Dijkstra
                             C: Floyd
                             D: Flujo máximo
                             E: Flujo a costo mínimo
                             F: Flujo a costo mínimo cotas

                             Elija una opción: """)
    if AlgoritmoRedes == "A" or AlgoritmoRedes == "a":
        Archivo8 = open("ArbolExpansionMinima.py")
        exec(Archivo8.read())

    elif AlgoritmoRedes == "B" or AlgoritmoRedes == "b":
        Archivo9 = open("Dijkstra.py")
        exec(Archivo9.read())

    elif AlgoritmoRedes == "C" or AlgoritmoRedes == "c":
        Archivo10 = open("Floyd.py")
        exec(Archivo10.read())
    
    elif AlgoritmoRedes == "D" or AlgortimoRedes == "d":
        Archivo11 = open("FlujoMaximo.py")
        exec(Archivo11.read())
    
    elif AlgortimoRedes == "E" or AlgoritmoRedes == "e":
        Archivo12 = open("FlujoCostoMinimo.py")
        exec(Archivo12.read())
    
    elif AlgoritmoRedes == "F" or AlgoritmoRedes == "f":
        Archivo13 = open("FlujoCostoMinimoCotas.py")
        exec(Archivo13.read())

elif Decision =="E" or Decision == "e":
    print("Selecciona el algoritmo de programación entera a usar:")
    AlgoritmoEntero = input(""" 
                              A: Ramificación y acotamiento
                              B: Enumeración implicita
                              C: Agente viajero

                              Elija una opción: """)
    if AlgoritmoEntero == "A" or AlgoritmoEntero == "a":
        Archivo14 = open("RamificacionAcotamiento.py")
        exec(Archivo14.read())

    elif AlgoritmoEntero == "B" or AlgoritmoEntero == "b":
        Archivo15 = open("EnumeracionImplicita.py")
        exec(Archivo15.read())
    
    elif AlgoritmoEntero == "C" or AlgoritmoEntero == "c":
        Archivo16 = open("AgenteViajero.py")
        exec(Archivo16.read())
else:
    print("Debes de seleccionar alguna de las opciones")
    print("Intenta de nuevo")

