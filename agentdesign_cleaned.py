import os 
import random 
import numpy as np
import pandas as pd 
from openai import OpenAI
from Networks.network import SocialNetwork
from Environments.policy import PolicyNetwork
from api_keys import open_ai_key
os.environ['OPENAI_API_KEY'] = open_ai_key

client = OpenAI() # Creating an instance that we will later use

global columns 
columns = ['Name', 'Characteristics'] # What we want to store in csv file.
db_directory = 'AgentDB'

if not os.path.exists(db_directory): # this is for making a new data base directory
    os.makedirs(db_directory)

class Agent:
    def __init__(self, name:str, agents, directory=db_directory):
        self.name = name
        self.social_network = SocialNetwork(agents)
        self.create_characteristics()
        # self.well_being = self.update_wellbeing() # not sure if this is necessary given that I already do this in the get_state function
        # Neural network model to decide action
        self.initial_state = self.get_state()
        self.action_dim = 2 # you talk or you don't talk
        self.policy_net = PolicyNetwork(self.initial_state.shape, self.action_dim) # creating a policy network here.
    
    def decide_action(self):
        state = self.get_state()
        actions = self.policy_net.predict(state) # giving you back the action that the agent should perform
        final_action = np.random.choice(self.action_dim, p=actions)
        final_action = np.where(actions == final_action)[0][0]
        # storing the actions as training data.
        # [...]
        self.perform_action(final_action)
        return final_action
        
    def update_wellbeing(self):
        self.degree = 0
        self.total_weight = 0
        for u,v in self.social_network.network.edges(f'{self.name}'):
            information = self.social_network.network.get_edge_data(u,v)
            self.total_weight += information['weight']
            self.degree += 1
        
        self.sociality = self.total_weight / self.degree
        self.well_being = (1-self.introversion) * self.sociality + self.introversion * self.degree
        return self.well_being
    
    def get_state(self):
        self.update_wellbeing()
        # self.update_characterstics()
        self.state = state = np.array([self.characteristics, self.total_weight, self.degree, self.well_being])
        return state
    
    def update_policy(self, reward, next_state):
        self.policy_net.update(self.get_state(), self.decide_action(), reward, next_state)
        
    def perform_action(self, action):
        # performing the action 
        if action == 0: 
            pass
        elif action == 1 :
            pass 
        pass
    
    def reward(self):
        return self.update_wellbeing()
    
    def create_characteristics(self):
        self.introversion = random.uniform(0,1) # uniformly giving each agent the attribute of introversion or extroversion on a spectrum vrom 0 to 1
        self.characteristics = self.introversion # this will change later depending on whether we want to implement more information on the states
        
    def prompt_creation(self):
        pass

# Setting up the agents
def agent_creation(agent_number, agents={}):
    with open('Agent_Information/information.txt', 'r') as f:
        content = f.readlines()
        content_names = [name.replace('\n', '') for name in content]
    # print(content_names)
    names = np.array([random.choice(content_names) for _ in range(agent_number)])
    for name in names:
        agents[name] = Agent(name, names)
        
    return agents # this is returning a dictionary

agents = agent_creation(5)

# for _, key in enumerate(agents):
#     print(agents[key].social_network.visualize())

