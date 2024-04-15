import numpy as np
import openai
from openai import Client
import networkx as nx
import os

"""
This is creating a novel pipelines as to how we can encode systems in python.
We are leveraging the novel capabilities of large language models, in oder to come up with a comprehensive module.
What is this going to fulfill? I don't know exactly yet, but we'll get there.

"""

client = Client()

# --------- CREATING SYSTEM DYNAMICS IN PYTHON IN A VERY SIMPLE WAY -------

class System():
    def __init__(self, elements: list, connections, purpose):
        self.elements = elements # is this is a list of agents? Or what is this?
        self.connections = connections
        self.purpose = purpose
        
    def initialize_network(self): 
        self.graph = nx.Graph()
        for element in self.elements: 
            self.graph.add_node(element)
        for connections in self.connections:
            src, dest = connections
            self.graph.add_edge(src, dest)
            
    
    def visualizing(self): 
        pass