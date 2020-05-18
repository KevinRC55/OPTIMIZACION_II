def Principal():
    Menu()

def Menu():
    print("************MENÚ PRINCIPAL**************")

    DecisionMenu = input("""
                      A: Transporte
                      B: Transbordo
                      C: Asignación
                      D: Redes
                      E: Programación entera 

                      Por favor seleccione una opción: """)

    if DecisionMenu == "A" or DecisionMenu =="a":
        Transporte()
    elif DecisionMenu == "B" or DecisionMenu =="b":
        Transbordo()
    elif DecisionMenu == "C" or DecisionMenu =="c":
        Asignacion()
    elif DecisionMenu == "D" or DecisionMenu =="d":
        Redes()
    elif DecisionMenu == "E" or DecisionMenu =="e":
        ProgramacionEntera()
    else:
        print("Debes de seleccionar alguna de las siguientes opciones A,B,C,D,E")
        print("Por favor intente de nuevo")
        Menu()



def Transporte():
    pass
def Transbordo():
    pass
def Asignacion():
    pass
def Redes():
    pass
def ProgramacionEntera():
    pass
    
Principal()



#salida =  open('EsquinaNoroesteTransporte.py')
#leer = salida.read()
#exec(leer)
