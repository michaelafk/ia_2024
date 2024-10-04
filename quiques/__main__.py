import sys
sys.path.append('C:/Users/michael/IA_2024')

from quiques import agent_amplada, agent_profunditat, agent_informat, joc


def main():
    # barca = agent_amplada.BarcaAmplada()
    # barca = agent_profunditat.BarcaProfunditat()
    barca = agent_informat.BarcaGreedy()
    illes = joc.Joc([barca])
    illes.comencar()


if __name__ == "__main__":
    main()
