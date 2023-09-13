def menu():
    opcion = "a"
    while opcion!= "d":
        print("que desea cotizar: ")
        print("1. Fiesta Gala")
        print("2. Fiesta Cumpleanios")
        print("d Detener programa")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1 or opcion == 2:
           cotizar_fiesta(int(opcion))
        elif opcion.lower() == "d":
            print("chao")    
        else:
            print("Opcion no valida")

def cotizar_fiesta(opcion:int):
    if opcion == 1:
        cotizar_fiesta_gala()
    else:
        cotizar_fiesta_cumpleanios()

def cotizar_fiesta_gala():
    pass

def cotizar_fiesta_cumpleanios():
    pass


menu()