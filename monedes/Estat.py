import copy
from quiques.joc import Joc

class Estat:
    def __init__(self,orden_monedes: str,cost: int,euristica: int,pare = None):
        if pare is None:
            self.cost = 0
        self.orden_monedes = orden_monedes
        self.cost = cost 
        self.euristica = calculate_euristic(self)
        self.pare = pare
   
def generar_fillsv2(self) -> list:
    index = self.orden_monedes.index(" ")
    succesors = []
    #PRIMERA ACCIO
    if index == 0:
        nou_estat = copy.deepcopy(self)
        nou_estat.orden_monedes = swap_characters(nou_estat.orden_monedes,index,index+1)
        nou_estat.pare = self
        nou_estat.cost +=1
        succesors.append(nou_estat)
    elif index == len(self.orden_monedes)-1:
        nou_estat = copy.deepcopy(self)
        nou_estat.orden_monedes = swap_characters(nou_estat.orden_monedes,index,index-1)
        nou_estat.pare = self
        nou_estat.cost +=1
        succesors.append(nou_estat)
    else:
        nou_estat = copy.deepcopy(self)
        nou_estat.orden_monedes = swap_characters(nou_estat.orden_monedes,index,index+1)
        nou_estat.pare = self
        nou_estat.cost +=1
        succesors.append(nou_estat)
        nou_estat1 = copy.deepcopy(self)
        nou_estat1.orden_monedes = swap_characters(nou_estat1.orden_monedes,index,index-1)
        nou_estat1.pare = self
        nou_estat.cost +=1
        succesors.append(nou_estat1)
    #SEGONA ACCIO
    for i in range(len(self.orden_monedes)):
        nou_estat = copy.deepcopy(self)
        aux = list(nou_estat.orden_monedes)
        if aux[i].__eq__("C"):
            aux[i] = "X"
        elif aux[i].__eq__("X"):
            aux[i] = "C"
        aux2 = ''.join(aux)
        if not aux2.__eq__(self.orden_monedes):
            nou_estat.orden_monedes = aux2
            nou_estat.pare = self
            nou_estat.cost +=2
            succesors.append(nou_estat)
    #TERCERA ACCIO
    for i in range(len(self.orden_monedes)):
        nou_estat = copy.deepcopy(self)
        aux = list(nou_estat.orden_monedes)
        if not aux[i].__eq__(" "):
            if aux[i].__eq__("C"):
                aux[i] = "X"
            else:
                aux[i] = "C"
            if i+2 < len(self.orden_monedes) - 1:
                aux2 = ''.join(aux)
                aux3 = swap_characters(aux2,i,i+2)
            else:
                aux2 = ''.join(aux)
                aux3 = swap_characters(aux2,i,i-2)
                nou_estat.orden_monedes = aux3
            nou_estat.pare = self
            nou_estat.cost +=2
            succesors.append(nou_estat)             
    return succesors

def swap_characters(s, i, j):
    if i != j:
    # Convert the string to a list to allow modifications
        s_list = list(s)
        # Swap the characters
        s_list[i], s_list[j] = s_list[j], s_list[i]
        # Convert the list back to a string
        s = ''.join(s_list)
    return s

def get_euristica(self):
    return self.euristica

def get_cost(self):
    return self.cost

def es_meta(self):
    return (self.orden_monedes.__eq__(" XXXC"))

def __lt__(self,other):
    """Overrides the default implementation"""
    return (
        self.euristica == other.euristica
    )

def calculate_euristic(self):
    orden_monedes_final = " XXXC"
    lista1 = list(orden_monedes_final)
    lista2 = list(self.orden_monedes)
    cont = 0
    for i in range(len(self.orden_monedes)):
        if i > 0:
            if lista1[i]!=lista2[i]:
                cont+=1 
        else:
            index1 = lista1.index(" ")
            index2 = lista2.index(" ")
            cont+= abs(index2-index1)
    return cont
