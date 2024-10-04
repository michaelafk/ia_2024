""" Fitxer que conté l'agent informat.

S'ha d'implementar el mètode:
    actua()
"""

from quiques.agent import Barca
from quiques.estat import Estat
from quiques.joc import AccionsBarca
from queue import PriorityQueue

class BarcaGreedy(Barca):
    def __init__(self):
        super(BarcaGreedy, self).__init__()

    def cerca(self, estat_inicial: Estat) -> bool:
        self.__per_visitar = []
        self.__visitats = set()
        exit = False

        self.__per_visitar.append(estat_inicial)
        while self.__per_visitar:
            estat_actual = self.__per_visitar.pop(-1)

            if estat_actual in self.__visitats or not estat_actual.es_segur():
                continue

            if estat_actual.es_meta():
                break

            for f in estat_actual.genera_fill():
                self.__per_visitar.append(f)

            self.__visitats.add(estat_actual)

        if estat_actual.es_meta():
            self.__cami_exit = estat_actual.cami
            exit = True

        return exit
    
    def actua(self, percepcio: dict) -> AccionsBarca | tuple[AccionsBarca, (int, int)]:
        pass
