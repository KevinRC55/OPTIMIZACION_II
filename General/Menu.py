import os
import sys


def MenuPrincipal():
    print("************MENÚ PRINCIPAL**************")

    Decision = input("""
                        A: Transporte
			B: Transbordo
			C: Asignación
			D: Redes
			E: Programación entera
			Ctrl+d: Salir

                        Elija una opción: """)

    os.system('clear')  # Linux
    # os.system('cls')   #Windows

    loop = True

    while loop:
        
        if Decision == "A" or Decision == "a":
            llamadoTransporte()
            Submenu()
        
        elif Decision == "B" or Decision =="b":
            llamadoTransbordo()
            Submenu()
        
        elif Decision == "C" or Decision =="c":
            llamadoAsignacion()
            Submenu()
        
        elif Decision =="D" or Decision =="d":
            llamadoRedes()
            Submenu()
        
        elif Decision =="E" or Decision == "e":
            llamadoProgramacionEntera()
            Submenu()
        
        elif Decision == "Q" or Decision == "q":
            break

        else:
            print("Debes de seleccionar alguna de las opciones")
            print("Intenta de nuevo")
            MenuPrincipal()

def llamadoTransporte():
    
    print("\nSelecciona el método de Transporte  a implementar:")
    AlgoritmoTransporte = input(""" 
                                    A: Esquina Noroeste
                                    B: Costo Mínimo
                                    C: Voguel

                                    Elija una opción: """)
    os.system('clear') #Linux
    # os.system('cls')   #Windows

    if AlgoritmoTransporte == "A" or AlgoritmoTransporte == "a":
        print("\n")
        os.system("python3 TransporteEsquinaNoroeste.py")    

    elif AlgoritmoTransporte == "B" or AlgoritmoTransporte == "b":
        print("\n")
        os.system("python3 TransporteCostoMinimo.py")
   
    elif AlgoritmoTransporte == "C" or AlgoritmoTransporte == "c":
        print("\n")
        os.system("python3 TransporteVogel.py")


def llamadoTransbordo():
    
    print("Selecciona el método de Transbordo  a implementar:")
    AlgoritmoTransbordo = input("""
				    A: Esquina Noroeste
				    B: Costo Minimo
				    C: Voguel

				    Elija una opción: """)
    
    os.system('clear') #Linux
    # os.system('cls')   #Windows


    if AlgoritmoTransbordo == "A" or AlgoritmoTransbordo == "a":
        os.system("python3 TransbordoEsquinaNoroeste.py")
    
    elif AlgoritmoTransbordo == "B" or AlgoritmoTransbordo == "b":
        os.system("python3 TransbordoCostoMinimo.py")
    
    elif AlgoritmoTransbordo == "C" or AlgoritmoTransbordo == "c":
        os.system("python3 TransbordoVoguel.py")
        

def llamadoAsignacion():
	
	print("Método Hungaro")
	os.system("python3 Hungaro.py")

        
def llamadoRedes():
    
    print("Selecciona el algoritmo de Redes a implementar:")
    AlgoritmoRedes = input(""" 
			      A: Arbol de expansión mínima
			      B: Dijkstra
			      C: Floyd
			      D: Flujo máximo
			      E: Flujo a costo mínimo
			      F: Flujo a costo mínimo cotas
								
			      Elija una opción: """)
	
    os.system('clear') #Linux
    # os.system('cls')   #Windows

    if AlgoritmoRedes == "A" or AlgoritmoRedes == "a":
        os.system("python3 ArbolExpansionMinima.py")
	
    elif AlgoritmoRedes == "B" or AlgoritmoRedes == "b":
        os.system("python3 Dijkstra.py")
		
    elif AlgoritmoRedes == "C" or AlgoritmoRedes == "c":
        os.system("python3 Floyd.py")
		
    elif AlgoritmoRedes == "D" or AlgoritmoRedes == "d":
        os.system("python3 FlujoMaximo.py")
		
    elif AlgoritmoRedes == "E" or AlgoritmoRedes == "e":
        os.system("python3 FlujoCostoMinimo.py")
	
    elif AlgoritmoRedes == "F" or AlgoritmoRedes == "f":
        os.system("python3 FlujoCostoMinimoCotas.py")
	
	
def llamadoProgramacionEntera():
    
    print("Selecciona el algoritmo de programación entera a usar:")
    AlgoritmoEntero = input(""" 
				A: Ramificación y acotamiento
				B: Enumeración implicita
				C: Agente viajero

				Elija una opción: """)
	
    os.system('clear') #Linux
    # os.system('cls')   #Windows

    if AlgoritmoEntero == "A" or AlgoritmoEntero == "a":
        os.system("python3 RamificacionAcotamiento.py")
		

    elif AlgoritmoEntero == "B" or AlgoritmoEntero == "b":
        os.system("python3 EnumeracionImplicita.py")
			
    elif AlgoritmoEntero == "C" or AlgoritmoEntero == "c":
        os.system("python3 AgenteViajero.py")		

def Submenu():
    
    print("\n¿Qué desea hacer?")
    Respuesta = input("""
			 A: Regresar al menu principal
			 B: Regresar al submenu
						 
			Elija una opción: """)
    
    os.system('clear') #Linux
    # os.system('cls')   #Windows


    if Respuesta == "A" or Respuesta == "a":
        MenuPrincipal()


MenuPrincipal()


