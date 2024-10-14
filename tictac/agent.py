"""

ClauPercepcio:
    POSICIO = 0
    OLOR = 1
    PARETS = 2
"""
import estat
from base import entorn
from tictac import joc


class Agent(joc.Agent):
    def __init__(self, nom):
        super(Agent, self).__init__(nom)
        self.__cami = None

    def pinta(self, display):
        pass

    def minimax(self,state: estat,torn):
        if evaluar(state,torn) != None:
            return estat,score
    def actua(
        self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        
        estat_inicial = estat(
            percepcio["Taulell"],percepcio["Agent"],None
        )

        return joc.Accio.ESPERAR
