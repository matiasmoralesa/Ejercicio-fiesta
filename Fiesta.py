class Fiesta:
    def __init__(self,numero_persona:int):
        self.__numero_persona = numero_persona
        self.__costo_decoracion = 0 
        if numero_persona > 12:    
            self.__bono_extra = 5000
        else:
            self.__bono_extra = 0     
        self.__costo_comida_persona = 3500
        self.__decora = False

    def calcular_costo_decoracion(self,decora:bool):
        if decora:
            if self.__numero_personas > 20:    
                self.__costo_decoracion = 22000 * self.__numero_personas
            else:
                self.__costo_decoracion = 16000 * self.__numero_personas

    def calcurar_costo(self):
        costo_comida = self.__costo_comida_persona * self.__numero_persona
        total = self.__costo_decoracion + costo_comida + self.__bono_extra 
        return total    