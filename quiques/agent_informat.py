""" Fitxer que conté l'agent informat.

S'ha d'implementar el mètode:
    actua()
"""

from quiques.agent import Barca
from quiques.estat import Estat
from quiques.joc import AccionsBarca
from queue import PriorityQueue
import math

class BarcaGreedy(Barca):
    def __init__(self):
        super(BarcaGreedy, self).__init__()
        self.__per_visitar = None
        self.__visitats = None
        self.__cami_exit = None

    def cerca(self, estat_inicial: Estat) -> bool:
        self.__per_visitar = PriorityQueue()
        self.__visitats = set()
        exit = False

        self.__per_visitar.put((self.heuristica(estat_inicial),estat_inicial))
        while self.__per_visitar:
            estat_actual = self.__per_visitar.get()[1]

            if estat_actual in self.__visitats or not estat_actual.es_segur():
                continue

            if estat_actual.es_meta():
                break

            for f in estat_actual.genera_fill():
                self.__per_visitar.put((self.heuristica(f),f))

            self.__visitats.add(estat_actual)

        if estat_actual.es_meta():
            self.__cami_exit = estat_actual.cami
            exit = True

        return exit
    
    def heuristica(self,estat : Estat):
        tupla_del_estat = (estat.quica_esq,estat.llops_esq)
        tupla_final = (0,0)
        resta_tuplas = (tupla_del_estat[0]-tupla_final[0],tupla_del_estat[1]-tupla_final[1])
        suma = resta_tuplas[0]**2 + resta_tuplas[1]**2
        arrel_quadrada = math.sqrt(suma)
        return arrel_quadrada
        
    
    def actua(self, percepcio: dict) -> AccionsBarca | tuple[AccionsBarca, (int, int)]:
        if self.__cami_exit is None:
            estat_inicial = Estat(
                local_barca=percepcio["Lloc"],
                llops_esq=percepcio["Llop Esq"],
                polls_esq=percepcio["Poll Esq"],
            )

            self.cerca(estat_inicial)

        if self.__cami_exit:
            quiques, llops = self.__cami_exit.pop(0)

            return AccionsBarca.MOURE, (quiques, llops)
        else:
            return AccionsBarca.ATURAR
    
