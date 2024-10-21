import copy
from practica.joc import Accions

class Estat:
    def __init__(self, taulell, Desti , Parets, pos ,cami_accions = None):
        if cami_accions is None:
            cami_accions = []
        self.taulell = taulell
        self.Desti = Desti
        self.Parets = Parets
        self.pos = pos
        self.cami_accions = cami_accions

    def generar_fills(self):
        #primeraccio MOURE JUGADOR ALS PUNTS CARDINALS
        #terceraaccio POSAR PARED
        #Nord
        succesors = []
        if self.pos[0] > 0:
            if (self.pos[0]-1,self.pos[1]) not in self.Parets and self.taulell[self.pos[0] - 1][self.pos[1]] != "O":
                nou_estat = copy.deepcopy(self)
                nou_estat.pos = (nou_estat.pos[0] - 1, nou_estat.pos[1])
                nou_estat.cami_accions + [(Accions.MOURE,"N")]
                succesors.append(nou_estat)
                #posar paret
                nou_estat1 = copy.deepcopy(self)
                nou_estat1.Parets + [(nou_estat1.pos[0] - 1, nou_estat1.pos[1])]
                nou_estat1.cami_accions + [(Accions.POSAR_PARET,"N")]
                succesors.append(nou_estat1)
        #West
        if self.pos[1] > 0:
            if (self.pos[0],self.pos[1]-1) not in self.Parets and self.taulell[self.pos[0]][self.pos[1] - 1] != "O":
                nou_estat = copy.deepcopy(self)
                nou_estat.pos = (nou_estat.pos[0] , nou_estat.pos[1] - 1)
                nou_estat.cami_accions + [(Accions.MOURE,"O")]
                succesors.append(nou_estat)
                #posar paret
                nou_estat1 = copy.deepcopy(self)
                nou_estat1.Parets + [(nou_estat1.pos[0], nou_estat1.pos[1]-1)]
                nou_estat1.cami_accions + [(Accions.POSAR_PARET,"O")]
                succesors.append(nou_estat1)
            
        #East
        if self.pos[1] < len(self.taulell) - 1:
            if (self.pos[0],self.pos[1]+1) not in self.Parets and self.taulell[self.pos[0]][self.pos[1] + 1] != "O":
                nou_estat = copy.deepcopy(self)
                nou_estat.pos = (nou_estat.pos[0] , nou_estat.pos[1] + 1)
                nou_estat.cami_accions + [(Accions.MOURE,"E")]
                succesors.append(nou_estat)
                #posar paret
                nou_estat1 = copy.deepcopy(self)
                nou_estat1.Parets + [(nou_estat1.pos[0], nou_estat1.pos[1]+1)]
                nou_estat1.cami_accions + [(Accions.POSAR_PARET,"E")]
                succesors.append(nou_estat1)    
        #South
        if self.pos[0] < len(self.taulell) - 1:
            if (self.pos[0]+1,self.pos[1]) not in self.Parets and self.taulell[self.pos[0] + 1][self.pos[1]] != "O":
                nou_estat = copy.deepcopy(self)
                nou_estat.pos = (nou_estat.pos[0] + 1, nou_estat.pos[1])
                nou_estat.cami_accions + [(Accions.MOURE,"S")]
                succesors.append(nou_estat)
                #posar paret
                nou_estat1 = copy.deepcopy(self)
                nou_estat1.Parets + [(nou_estat1.pos[0] + 1, nou_estat1.pos[1])]
                nou_estat1.cami_accions + [(Accions.POSAR_PARET,"S")]
                succesors.append(nou_estat1)    
        #segonaaccio BOTAR JUGADOR ALS PUNTS CARDINALS
        #Nord
        if self.pos[0] > 1:
            if (self.pos[0]-2,self.pos[1]) not in self.Parets and self.taulell[self.pos[0] - 2][self.pos[1]] != "O":
                nou_estat = copy.deepcopy(self)
                nou_estat.pos = (nou_estat.pos[0] - 2, nou_estat.pos[1])
                nou_estat.cami_accions + [(Accions.BOTAR,"N")]
                succesors.append(nou_estat)
        #West
        if self.pos[1] > 1:
            if (self.pos[0],self.pos[1]-2) not in self.Parets and self.taulell[self.pos[0]][self.pos[1] - 2] != "O":
                nou_estat = copy.deepcopy(self)
                nou_estat.pos = (nou_estat.pos[0] , nou_estat.pos[1] - 2)
                nou_estat.cami_accions + [(Accions.BOTAR,"O")]
                succesors.append(nou_estat)
            
        #East
        if self.pos[1] + 2 < len(self.taulell):
            if (self.pos[0],self.pos[1]+2) not in self.Parets and self.taulell[self.pos[0]][self.pos[1] + 2] != "O":
                nou_estat = copy.deepcopy(self)
                nou_estat.pos = (nou_estat.pos[0] , nou_estat.pos[1] + 2)
                nou_estat.cami_accions + [(Accions.BOTAR,"E")]
                succesors.append(nou_estat)    
        #South
        if self.pos[0] + 2 < len(self.taulell):
            if (self.pos[0]+2,self.pos[1]) not in self.Parets and self.taulell[self.pos[0] + 2][self.pos[1]] != "O":
                nou_estat = copy.deepcopy(self)
                nou_estat.pos = (nou_estat.pos[0] + 2, nou_estat.pos[1])
                nou_estat.cami_accions + [(Accions.BOTAR,"S")]
                succesors.append(nou_estat)       
        return succesors  
           
    def es_meta(self):
        return self.pos == self.Desti