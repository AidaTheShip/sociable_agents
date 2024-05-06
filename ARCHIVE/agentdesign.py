import os 
import random 
import numpy as np
import pandas as pd 
from openai import OpenAI
# from network import SocialNetwork
# from policy import PolicyNetwork # this takes forever
from api_keys import open_ai_key
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
os.environ['OPENAI_API_KEY'] = open_ai_key

client = OpenAI() # Creating an instance that we will later use

class Agent:
    def __init__(self, name, environment, first=True):
        self.name = name
        self.social_network = environment # this is the overall social network, the agent is going to participate in.
        # self.initial_state = self.get_state()
        self.state_dim = 4
        self.initial_state = np.zeros((self.state_dim))
        self.action_dim = 2
        # self.policy_net = PolicyNetwork(self.initla_state.shape, self.action_dim)
        # Setting up some characteristics for the agents
        if first: 
            self.characteristics = self.create_characteristics() # creating characteristics of the agent and storing it in here but only if they are initiated for teh first time.
            
    
    def get_state(self): 
        self.update_wellbeing()
        # We might have to change the state to something different later on. It might have to depend a bit more on the actual social network
        self.state = np.array([self.characteristics, self.well_being, self.degree, self.total_weight]) # check whether I have to update this a bit more.
        return self.state
    
    def decide_action(self):
        state = self.get_state()
        actions = self.policy_net.predict(state) # giving you back the actin that the agent should perform
        final_action = np.random.choice(self.action_dim, p=actions)
        final_action = np.where(actions == final_action)[0][0] # this will give you an integer value based on which you will either do one of the two actions. Discretizing
        
        self.perform_action(final_action)
        
        # Storing the actions as training data
    
    def perform_action(self, action):
        # Actions might have to be a bit more than just updating the network, e.g., the people you interact with, then this is where you have to change it.
        # performing the action / picking a random interaction 
        if action == 0: # you are talking
            # This has to change. 
            interaction_partner = random.choice(self.information)
            quality_conversation = random.uniform(0,1) # this will be replaced by an LLM evaluation
            self.social_network.update_connection(interaction_partner, quality_conversation)
            
        elif action == 1 : # this is not interacting.
            pass
        
        old_state = self.state
        next_state = self.get_state()
        reward = self.well_being # the higher the well-being the higher the reward? 
        # YOU STILL HAVE TO DEFINE WHERE THE REWARD COMES IN. 
        self.policy_net.update(old_state, self.action, self.reward, next_state)
        return old_state, action, next_state, reward
            
    def update_wellbeing(self):
        self.degree = 0
        self.total_weight = 0
        for u,v in self.social_network.network.edges(f'{self.name}'):
            self.information = self.social_network.network.get_edge_data(u,v)
            self.total_weight += self.information['weight']
            self.degree += 1
        self.sociality = self.total_weight / self.degree
        self.well_being = (1-self.introversion)*self.sociality+ self.introversion*self.degree
        return self.well_being
    
    def create_characteristics(self):
        self.introversion = random.uniform(0,1)
        self.characteristics = self.introversion # for now this is just introversion

# A = Agent("Nino", None)