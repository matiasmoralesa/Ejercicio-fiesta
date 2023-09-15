from FiestaCumpleanios import FiestaCumpleanios
from FiestaGala import FiestaGala

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
    try:
        personas = int(input('Ingrese numero de personas: '))
        if personas > 0:
           gala = FiestaGala(personas)
           gala.calcular_costo_decoracion(decidete('decorar'))
           gala.set_opcion_saludable(decidete('opcion saludable'))
           total = gala.calcurar_costo
           print(gala)
           print(f'total: {total}')
        else:
            print('ERROR.-Debes ingresar un valor mayor a 1')
    except:
        print('ERROR.-Debes ingresar un valor entero')    

def cotizar_fiesta_cumpleanios():
    pass


def decidete(texto:str):
    decide = 'a'
    while decide != 's' and decide != 'n':
        decide = input(f'Desea {texto}: s/n ')
        if decide.lower() == 's':
            return True
        elif decide.lower('n'):
            return False
        else:
            print('ERROR.- Solo puedes ingresar s o n')


menu()