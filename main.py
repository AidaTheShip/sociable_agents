import networkx as nx
from network import SocialNetwork
import numpy as np
import random
from agentdesign import Agent

def setup(num_agents, agents={}):
    try:
        with open('Agent_Information/information.txt', 'r') as f:
            content = f.readlines()
        content_names = [name.strip() for name in content]  # Using strip() to remove any leading/trailing whitespace

        if content_names:  # Check if the list is not empty
            names = np.array([random.choice(content_names) for _ in range(num_agents)])
            # print(names)
        else:
            print("No names are available in the file.")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Create general social network based on the agents
    network = SocialNetwork(names) # this is instantiating a network with all the agents that will be in the simulation but with no connection initially.
    # Create each agent with the knowledge of the social network
    # for name in names:
    #     agents[name] = Agent(name, network)
        
    
    return agents, network

a = Agent("H", None)

# participants, network = setup(3)
# # print(participants)
# print(participants, network)
# print(network.network.edges)

# test = SocialNetwork(['a', 'b', 'c'])
# print(test.network.edges)