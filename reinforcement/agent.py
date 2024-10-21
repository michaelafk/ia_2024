import logging
import random

import numpy as np

from base import entorn
from reinforcement.abstractmodel import AbstractModel
from reinforcement.joc import Status


class AgentQ(AbstractModel):
    """Tabular Q-learning prediction model.

    For every state (here: the agents current location ) the value for each of the actions is
    stored in a table.The key for this table is (state + action). Initially all values are 0.
    When playing training games after every move the value in the table is updated based on
    the reward gained after making the move. Training ends after a fixed number of games,
    or earlier if a stopping criterion is reached (here: a 100% win rate).
    """

    default_check_convergence_every = (
        5  # by default check for convergence every # episodes
    )

    def __init__(self, game, **kwargs):
        """Create a new prediction model for 'game'.

        Args:
            game (Maze): Maze game object
            kwargs: model dependent init parameters
        """
        super().__init__(game, name="QTableModel")
        self.Q = {}  # table with value for (state, action) combination

    def q(self, state):
        """Get q values for all actions for a certain state."""
        if type(state) is np.ndarray:
            state = tuple(state.flatten())

        q_aprox = np.zeros(len(self.environment.actions))
        i = 0
        for action in self.environment.actions:
            if (state, action) in self.Q:
                q_aprox[i] = self.Q[(state, action)]
            i += 1

        return q_aprox

    def actua(self, percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        """Policy: choose the action with the highest value from the Q-table. Random choice if
        multiple actions have the same (max) value.

        Args:
            percepcio: game state
        Returns:
            selected action
        """
        q = self.q(percepcio["POS"])

        actions = np.nonzero(q == np.max(q))[
            0
        ]  # get index of the action(s) with the max value
        return random.choice(actions)

    def pinta(self, display) -> None:
        pass

    def predict(self, state):
        """Policy: choose the action with the highest value from the Q-table.
        Random choice if multiple actions have the same (max) value.

        :param np.ndarray state: game state
        :return int: selected action
        """
        q = self.q(state)

        actions = np.nonzero(q == np.max(q))[
            0
        ]  # get index of the action(s) with the max value
        return self.environment.actions[random.choice(actions)]

    def train(
        self,
        discount,
        exploration_rate,
        learning_rate,
        episodes,
        stop_at_convergence=False,
    ):
        """Train the model

        Args:
            stop_at_convergence: stop training as soon as convergence is reached.

        Hyperparameters:
            discount (float): (gamma) preference for future rewards (0 = not at all, 1 = only)
            exploration_rate (float): exploration rate reduction after each random step
                                (<= 1, 1 = no at all)
            learning_rate (float): preference for using new knowledge (0 = not at all, 1 = only)
            episodes (int): number of training games to play

        Returns:
            Int, datetime: number of training episodes, total time spent
        """

        # variables for reporting purposes
        cumulative_reward = 0
        cumulative_reward_history = []
        win_history = []

        # start_time = datetime.now()

        # training starts here
        for episode in range(1, episodes + 1):

            state = self.environment.reset()

            while True:
                # choose action epsilon greedy
                if np.random.random() < exploration_rate:
                    action = random.choice(self.environment.actions)
                else:
                    action = self.predict(state)

                next_state, reward, status = self.environment._aplica(action)
                cumulative_reward += reward

                if (
                    state,
                    action,
                ) not in self.Q.keys():  # ensure value exists for (state, action)
                    # to avoid a KeyError
                    self.Q[(state, action)] = 0.0

                # FORA POLÍTICA!
                max_next_Q = 0
                for a in self.environment.actions:
                    if (next_state, a) in self.Q and self.Q[
                        (next_state, a)
                    ] > max_next_Q:
                        max_next_Q = self.Q[(next_state, a)]

                self.Q[(state, action)] = self.Q[(state, action)] + learning_rate * (
                    reward + discount * max_next_Q - self.Q[(state, action)]
                )

                if status in (
                    Status.WIN,
                    Status.LOSE,
                ):  # terminal state reached, stop episode
                    break

                state = next_state

            cumulative_reward_history.append(cumulative_reward)

            logging.info(
                "episode: {:d}/{:d} | status: {:4s} | e: {:.5f}".format(
                    episode, episodes, status.name, exploration_rate
                )
            )
        """
            if episode % check_convergence_every == 0:
                # check if the current model does win from all starting cells
                # only possible if there is a finite number of starting states
                w_all, win_rate = self.environment.check_win_all(self)
                win_history.append((episode, win_rate))
                if w_all is True and stop_at_convergence is True:
                    logging.info("won from all start cells, stop learning")
                    break
        """

        logging.info("episodes: {:d}".format(episode))

        return cumulative_reward_history, win_history, episode
