# from agentdesign import Agent
import numpy as np 
import networkx as nx
from pyvis.network import Network

class SocialNetwork(): 
    # Enter the agents as a string of lists.
    def __init__(self, agents: list[str], curr_network:np.matrix=None): 
        self.participants = agents # this stores all the agents that are in the simulation
        self.initializing_network(curr_network)
        self.vis = 0
    
    def update_connection(self, connection:tuple, strength:float=None):
        # Pyvis is mainly used for visualization but we will work around this by continuously updating the networkx data structure that is underlying
        # when you meet someone new, then you're going to establish a new connection
        src, dir = connection
        
        # For now, we will not allow any new agents to be created. Every agent has a connection with the every other one already in the network.
        # What remains is just updating the weight.
        self.network[src][dir]['weight'] = strength

    def remove_connection(self, connection:tuple):
        src, dir = connection
        self.network[src][dir]['weight'] = 0
        
    def initializing_network(self, adjacency_matrix:np.matrix=None):
        # Connections should include: source, target; initial weights should include the initial weights
        # This function initializes the nodes of the network + adjacency matrix 
        dimension = len(self.participants)
        # this establishes the connections if there are any
        # if adjacency_matrix is None or []:
        #     print("Its none")
        #     self.adjacency_matrix = np.zeros(shape=(dimension, dimension))
            
        # else: 
        #     self.adjacency_matrix=adjacency_matrix
            
        net = nx.Graph()
        # Adding the nodes into the network 
        # for i in range(dimension):
        #     net.add_node(i, label=self.participants[i]) # note that you can also add a positon of the node here and some other properties; might be interesting
        
        # Adding the connections
        # rows, columns = self.adjacency_matrix.shape
        rows, columns = dimension, dimension
        for i in range(rows): 
            for j in range(columns):
                if i != j: # making sure that there is no self-relationship in here. we might change this later. 
                    net.add_edge(self.participants[i], self.participants[j], weight=0) # setting the ninital weights to zero 
                    
        self.network = net
    
    def create_adjacency_matrix(self):    
        self.adjacency_matrix = np.matrix(nx.adjacency_matrix(self.network).todense())
        
    def visualize(self):
        nt = Network(notebook=True)
        self.vis += 1
        nt.from_nx(self.network)
        nt.show('network.html')
    
    def reset(self): 
        self.network = self.initializing_network()

        
# Testing class functionality

test = SocialNetwork(['a', 'b', 'c'])
print(test.network.graph) # yay, it works!
# a = test.network.edges('a')[0]['weight']
for u,v in test.network.edges('a'):
    print(u,v, test.network.get_edge_data(u, v)['weight'])
    
    # print(edge['weight'])
# print(test.network.edges('a'))
# print(test.network.edges('1'))
# test.visualize()
# print(test.network.nodes)
# print(test.network.nodes['b'])
# test.reset()