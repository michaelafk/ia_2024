import sys
sys.path.append('C:/Users/kirky/IA_2024')
from aspirador import joc_gui, agent

def main():
    # agents = [agent.AspiradorTaula()]
    # agents = [agent.AspiradorReflex()]
    agents = [agent.AspiradorMemoria()]
    hab = joc_gui.Aspirador(agents)
    hab.comencar()


if __name__ == "__main__":
    main()
