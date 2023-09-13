from Fiesta import Fiesta
class FiestaGala(Fiesta):
    def __init__(self,numero_persona:int):
        Fiesta(numero_persona)
        self.__costo_fijo_personas = 2000
        self.__opcion_saludable = False

    def set_opcion_saludable(self,opcion_saludable:bool):
        self.__opcion_saludable = opcion_saludable
        if opcion_saludable:
            self.__costo_fijo_personas = 4000

    def calcurar_costo(self):
        costo_fiesta = super().calcurar_costo()
        costo_gala = self.__costo_fijo_personas * super().__numero_persona
        total = costo_fiesta + costo_gala
        return total        