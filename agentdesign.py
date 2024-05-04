import os 
import random 
import numpy as np
import pandas as pd 
from openai import OpenAI
# from network import SocialNetwork
# from policy import PolicyNetwork # this takes forever
from api_keys import open_ai_key
os.environ['OPENAI_API_KEY'] = open_ai_key

client = OpenAI() # Creating an instance that we will later use

# global columns 
columns = ['Name', 'Characteristics'] # What we want to store in csv file.
db_directory = 'AgentDB'

if not os.path.exists(db_directory): # this is for making a new data base directory
    os.makedirs(db_directory)

class Agent:
    def __init__(self, name, environment, db_dictionary=db_directory):
        self.name = name
        self.social_network = environment # this is the overall social network, the agent is going to participate in.
        # self.initial_state = self.get_state()
        self.state_dim = 4
        self.initial_state = np.zeros((self.state_dim))
        self.action_dim = 2
        # self.policy_net = PolicyNetwork(self.initla_state.shape, self.action_dim)
        # Setting up some characteristics for the agents
    
    def get_state(self): 
        self.update_wellbeing()
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
        # performing the action / picking a random interaction 
        if action == 0: # you are talking
            interaction_partner = random.choice(self.information)
            quality_conversation = random.uniform(0,1)
            self.social_network.update_connection(interaction_partner, quality_conversation)
            
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


A = Agent("Nino", None)