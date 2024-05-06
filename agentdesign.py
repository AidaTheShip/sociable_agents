import random
from policy import PolicyNetwork
import numpy as np

class Agent:
    def __init__(self, name, environment):
        self.name = name
        self.social_network = environment
        self.state_dim = 4
        self.action_dim = 2
        self.create_characteristics()
        self.policy_net = PolicyNetwork(self.state_dim, self.action_dim)

    def get_state(self):
        self.update_wellbeing()
        return [self.introversion, self.well_being, float(self.degree), float(self.total_weight)]

    def action(self):
        state = self.get_state()
        action_prob = self.policy_net.predict(state)
        action = np.random.choice(self.action_dim, p=action_prob.detach().numpy()[0])
        if action == 0:
            interaction_partner = random.choice(list(self.social_network.network.edges(self.name)))
            quality_conversation = random.uniform(0, 1)
            self.social_network.update_connection(interaction_partner, quality_conversation)
        old_state = state
        next_state = self.get_state()
        reward = self.well_being
        return old_state, action, next_state, reward

    def update_wellbeing(self):
        self.degree = 0
        self.total_weight = 0
        for u, v in self.social_network.network.edges(self.name):
            self.total_weight += self.social_network.network[u][v]['weight']
            self.degree += 1
        self.sociality = self.total_weight / max(1, self.degree)  # Avoid division by zero
        self.well_being = (1 - self.introversion) * self.sociality + self.introversion * self.degree

    def create_characteristics(self):
        self.introversion = random.uniform(0, 1)