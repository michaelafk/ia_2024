import random

from practica import joc
from practica.joc import Accions
from practica.Estat import Estat

class Viatger(joc.Viatger):
    def __init__(self, *args, **kwargs):
        super(Viatger, self).__init__(*args, **kwargs)
        self.per_visitar = None
        self.visitats = None
        self.cami_exit = None

    def pinta(self, display):
        pass
    
    def cerca(self,estat_inicial: Estat):
        self.per_visitar = []
        self.visitats = set()
        exit = False
        
        self.per_visitar.append(estat_inicial)
        while self.per_visitar:
            estat_actual = self.per_visitar.pop(-1)
            
            if estat_actual in self.visitats:
                continue
            if estat_actual.es_meta():
                break
            
            for fills in estat_actual.generar_fills():
                self.per_visitar.append(fills)
            
            self.visitats.add(estat_actual)
            
        if estat_actual.es_meta():
            self.cami_exit = estat_actual.cami_accions
            exit = True
        
        return exit
        
        

    def actua(self, percepcio: dict) -> Accions | tuple[Accions, str]:
        if self.cami_exit is None:
            estat_inicial = Estat (
                taulell = percepcio["TAULELL"],
                Desti = percepcio["DESTI"],
                Parets = percepcio["PARETS"],
                pos = percepcio["AGENTS"],
                cami_accions = None
            )
            self.cerca(estat_inicial)
            
        if self.cami_exit:
            return self.cami_exit.pop(0)
        else:
            return Accions.ESPERAR
