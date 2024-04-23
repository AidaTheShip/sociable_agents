import os 
import random 
import numpy as np
import pandas as pd 
from openai import OpenAI
from Networks.network import SocialNetwork
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
        self.well_being = self.create_characteristics()
        
    def create_characteristics(self):
        self.introversion = random.uniform(0,1) # uniformly giving each agent the attribute of introversion or extroversion on a spectrum vrom 0 to 1
        self.degree = 0
        self.total_weight = 0
        for u,v in self.social_network.network.edges(f'{self.name}'):
            information = self.social_network.network.get_edge_data(u,v)
            self.total_weight += information['weight']
            self.degree += 1
        
        self.sociality = self.total_weight / self.degree
        self.well_being = (1-self.introversion) * self.sociality + self.introversion * self.degree
    
    

    
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

