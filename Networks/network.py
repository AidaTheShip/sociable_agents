# from agentdesign import Agent
import numpy as np 
import networkx as nx
from pyvis.network import Network

class SocialNetwork(): 
    # Enter the agents as a string of lists.
    def __init__(self, agents: list[str], curr_network:np.matrix=None): 
        self.participants = agents # this stores all the agents that are in the simulation
        self.initializing_network(curr_network)
    
    def update_connection(self, connection:tuple, strength:float=None):
        # Pyvis is mainly used for visualization but we will work around this by continuously updating the networkx data structure that is underlying
        # when you meet someone new, then you're going to establish a new connection
        src, dir = connection
        
        # For now, we will not allow any new agents to be created. Every agent has a connection with the every other one already in the network.
        # What remains is just updating the weight.
        self.network[src][dir]['weight'] = strength

    
    def initializing_network(self, adjacency_matrix:np.matrix=None):
        # Connections should include: source, target; initial weights should include the initial weights
        # This function initializes the nodes of the network + adjacency matrix 
        dimension = len(self.participants)
        # this establishes the connections if there are any
        self.adjacency_matrix = np.zeros(shape=(dimension, dimension))
        # if adjacency_matrix is None or []:
        #     print("Its none")
        #     self.adjacency_matrix = np.zeros(shape=(dimension, dimension))
            
        # else: 
        #     self.adjacency_matrix=adjacency_matrix
            
        net = nx.Graph()
        # Adding the nodes into the network 
        for i in range(dimension):
            net.add_node(i, label=self.agents[i]) # note that you can also add a positon of the node here and some other properties; might be interesting
        
        # Adding the connections
        # rows, columns = self.adjacency_matrix.shape
        rows, columns = dimension, dimension
        for i in range(rows): 
            for j in range(columns):
                net.add_edge(i, j, weight=self.adjacency_matrix[i][j])
        
        self.network = net
    
        
    def visualize(self):
        nt = Network(notebook=True)
        nt.from_nx(self.G)
        nt.show('network.html')

        
        
        
        

# Testing class functionality
test = SocialNetwork(['a', 'b', 'c'], [])
print(test.network.graph) # yay, it works!
