from Fiesta import Fiesta
class FiestaCumpleanios(Fiesta):
    def __init__(self, numero_persona:int):
        Fiesta(numero_persona)
        self.__valor_pastel = 0
        self.__texto_pastel = ''

    def personalizar_pastel(self,texto_pastel:str):
        self.__texto_pastel = texto_pastel

    def calcular_costo(self):
        costo_fiesta: super().calcurar_costo()
        costo_cumpleanios: self.__valor_pastel 
        total = costo_fiesta + costo_cumpleanios
        return total 
     

    def calcular_costo_pastel(self,):
        if self.__texto_pastel != '':
            if self.__numero_persona > 4:
                self.__valor_pastel = 10000
            else:
                self.__valor_pastel = 5000