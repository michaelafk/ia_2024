""" Mòdul que conté l'agent per jugar al joc de les monedes.

Percepcions:
    ClauPercepcio.MONEDES
Solució:
    " XXXC"
"""
from queue import PriorityQueue
from base import agent, entorn
from monedes.joc import AccionsMoneda,Estat

SOLUCIO = " XXXC"


class AgentMoneda(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=0)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def pinta(self, display):
        print(self._posicio_pintar)

    def cerca(self, estat_inicial: Estat) -> bool:
        self.__oberts = PriorityQueue()
        self.__tancats = set()
        exit = False

        self.__oberts.put((estat_inicial.get_euristica() + estat_inicial.get_cost()),estat_inicial)
        while self.__oberts:
            estat_actual = self.__oberts.get()[1]

            if estat_actual in self.__tancats:
                continue

            if estat_actual.es_meta():
                break

            for f in estat_actual.genera_fill():
                self.__oberts.put((f.get_euristica() + f.get_cost()),f)

            self.__tancats.add(estat_actual)

        if estat_actual.es_meta():
            self.__accions = self.__tancats
            exit = True

        return exit
    def actua(
        self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:        
        if self.__accions is None:
            estat_inicial = Estat(
                orden_monedes = "CX CX"
            )
            self.cerca(estat_inicial)

        if self.__tancats:
            estat = self.__cami_exit.pop(0)

            return AccionsMoneda.BOTAR, (quiques, llops)
        else:
            return AccionsBarca.ATURAR
        return AccionsMoneda.RES




