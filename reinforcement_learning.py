import numpy as np
import tensorflow
from keras import layers
from agentdesign import Agent, agent_creation
# from agentsetup import agent_creation
num_agents = 5

# Creating our agents
agents = agent_creation(num_agents) # this automatically creates 5 agents that are randomized based on their names


# Setting up the main training loop
def train_agent(episodes, agent):
    for episode in range(episodes): 
        pass
    
def simulation():
    # do it based on random walks as to when the agents even have the choice to interact with someone or not - is thsi making it a bit too complicated?
    pass
    
    
