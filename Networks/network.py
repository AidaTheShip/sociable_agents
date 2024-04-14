# from agentdesign import Agent
import numpy as np 
from pyvis.network import Network

class SocialNetwork(): 
    def __init__(self, agents: list, curr_network:np.matrix=None): 
        self.participants = agents # this stores all the agents that are in the simulation
        self.initializing_network(curr_network)
    
    def update(self, new_connectio:tuple, strength:float=None):
        # when you meet someone new, then you're going to establish a new connection
        pass
    
    def initializing_network(self, adjacency_matrix:np.matrix=None):
        # Connections should include: source, target; initial weights should include the initial weights
        # This function initializes the nodes of the network + adjacency matrix 
        dimension = len(self.participants)
        # this establishes the connections if there are any
        if adjacency_matrix is None:
            self.adjacency_matrix = np.zeros(shape=(dimension, dimension))
            
        else: 
            self.adjacency_matrix=adjacency_matrix
            
        net = Network()
        # Adding the nodes into the network 
        for i in range(dimension):
            net.add_node(i, label=f"Agent {i}") # note that you can also add a positon of the node here and some other properties; might be interesting
        
        # Adding the connections
        rows, columns = self.adjacency_matrix.shape
        for i in range(rows): 
            for j in range(columns):
                net.add_edge(i, j, value=self.adjacency_matrix[i][j])
        
        self.network = net
    
        
    def visualize(self):
        self.network.toggle_physics(True)
        self.network.show('Social network')
        
        
        
        

# # Testing class functionality
# test = SocialNetwork(['a', 'b', 'c'], [])
# print(test.adjacency_matrix)
