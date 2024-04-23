import numpy as np 
import random
from agentdesign import Agent
agent_number = 10


# ----------------------- CREATING AGENTS ---------------------------

def agent_creation(agent_number, agents = {}):
# For loop for instantiating x people
    with open('Agent_Information/information.txt', 'r') as f:
        content = f.readlines()
        content_names = [name.replace('\n', '') for name in content]
    # print(content_names)
    # Based on the number of agents we want, we can select random names
    names = np.array([random.choice(content_names) for _ in range(agent_number)])
    print(type(names))
    for name in names: 
        agents[name] = Agent(name)
        agents[name].social_network(names) # Initializing the social network of agents by passing in all the agents that are participating in the simulation
    
    return agents

agents = agent_creation(4)
for agent in agents: 
    print(agent)