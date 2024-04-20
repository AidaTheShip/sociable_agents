import random 
import numpy as np


class SocialEnvironment:
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.interaction_matrix = np.zeros((num_agents, num_agents))

    def reset(self):
        self.interaction_matrix = np.zeros((self.num_agents, self.num_agents))
        return np.zeros(self.num_agents) # Resetting the interactions ==> is there any way we can train each of the agents 
    # Train reinforcemnet learning within reinforfement leraning? 

    def step(self, actions):
        rewards = np.zeros(self.num_agents)
        for i in range(self.num_agents):
            if actions[i] == 1:  # Agent i chooses to talk
                for j in range(self.num_agents):
                    if i != j and actions[j] == 1:
                        # Update interaction matrix positively
                        self.interaction_matrix[i][j] += 1
                        rewards[i] += 1  # Simplified reward
        return rewards

    def get_state(self):
        # Return the current interaction matrix as the state
        return self.interaction_matrix
