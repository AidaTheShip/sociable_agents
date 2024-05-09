import random
from policy import PolicyNetwork
import numpy as np
import torch.distributions as distributions

# Define the Agent
class Agent:
    def __init__(self, name, environment, epsilon=0.01):
        self.name = name
        self.social_network = environment
        self.state_dim = 3
        self.action_dim = 2
        self.create_characteristics()
        self.policy_net = PolicyNetwork(self.state_dim, self.action_dim)
        self.epsilon = epsilon  # Exploration parameter
        self.reward_history = []  # To store the reward history for this agent

    def get_state(self):
        self.update_wellbeing()
        avg_connection_strength = self.total_weight / max(1, self.degree)
        state = [self.introversion, self.well_being, avg_connection_strength]
        return state

    def select_partner(self):
        # Strategically select partner based on connection strength
        edges = list(self.social_network.network.edges(self.name, data=True))
        if not edges:
            return None  # In case there are no edges
        # Choose the partner with the strongest connection
        selected_edge = max(edges, key=lambda x: x[2]['weight'])
        return (selected_edge[0], selected_edge[1])

    def action(self):
      state = self.get_state()
      action_prob = self.policy_net.predict(state) # What do I do with these? 

      if np.random.rand() < self.epsilon:
        action = np.random.choice(self.action_dim)
      else:
      # Sampling an action from the probability distribution 
        action_dist = distributions.Categorical(action_prob) # Look into this more deeply, change it potentially
        action = action_dist.sample().item() # this is taking one of the actions and performing it
    
      if action == 0: 
        interaction_partner = self.select_partner()
        if interaction_partner:
        # LLM will play in here in determining the quality of the conversation
          quality_conversation = random.uniform(0,1) # random quality conversation
          self.social_network.update_connection(interaction_partner, quality_conversation)
    
      old_state = state
      next_state = self.get_state()
      reward = self.well_being # this is a place to be augmented as well

      self.reward_history.append(reward) # Storing the reward for this state

      return old_state, action, next_state, reward
      
        # state = self.get_state()
        # action_prob = self.policy_net.predict(state)
        
        # # Exploration-exploitation strategy: ε-greedy
        # if np.random.rand() < self.epsilon:
        #     action = np.random.choice(self.action_dim)
        # else:
        #     # Sample action from the probability distribution
        #     action_dist = distributions.Categorical(action_prob)
        #     action = action_dist.sample().item()
        
        # if action == 0:
        #     interaction_partner = self.select_partner()
        #     if interaction_partner:
        #         quality_conversation = random.uniform(0, 1)  # Random quality conversation
        #         self.social_network.update_connection(interaction_partner, quality_conversation)
        
        # old_state = state
        # next_state = self.get_state()
        # reward = self.well_being
        # self.reward_history.append(reward)  # Store the reward for this step
        # return old_state, action, next_state, reward

    def update_wellbeing(self):
        self.degree = 0
        self.total_weight = 0
        for u, v in self.social_network.network.edges(self.name):
            self.total_weight += self.social_network.network[u][v]['weight']
            if self.social_network.network[u][v]['weight'] != 0.0:
              self.degree += 1
        self.sociality = self.total_weight / max(1, self.degree)
        # self.well_being = (1 - self.introversion) * self.sociality + self.introversion * self.degree)
        self.well_being = (self.introversion) * self.sociality + self.introversion * self.degree

    def create_characteristics(self):
        self.introversion = random.uniform(0, 1)