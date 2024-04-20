import numpy as np
import tensorflow
from keras import layers
from agentdesign import Agent
from agentsetup import agent_creation
num_agents = 5

agents = agent_creation(num_agents)

for agent in agents: 
    print(agent.name)