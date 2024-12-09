import sys
sys.path.append('C:/Users/kirky/IA_2024')

import logging

from reinforcement.agent import AgentQ
from reinforcement.joc import Laberint


def main():
    logging.basicConfig(
        format="%(levelname)-8s: %(asctime)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )  # Only show messages *equal to or above* this level

    game = Laberint()
    agent = AgentQ(game)
    h, w, _ = agent.train(
        discount=0.90,
        exploration_rate=0.10,
        learning_rate=0.6,
        episodes=1000,
        stop_at_convergence=True,
    )
    valores = []
    for i in range(4):
        valores.append(agent.Q[(0,0),i])
    valores.sort()
    for valor in valores:
        print(valor)
    max = valores.pop(-1)
    print(max)
    game.reset()
    game.set_agent([agent])
    game.comencar()


if __name__ == "__main__":
    main()