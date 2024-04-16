import numpy as np
import openai
from openai import Client
import networkx as nx
import os
from api_keys import open_ai_key
os.environ['OPENAI_API_KEY'] = open_ai_key

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
        self.purpose = purpose # this is given here.
        
    def initialize_network(self): # mapping the connection between the elements
        self.graph = nx.Graph()
        for element in self.elements: 
            self.graph.add_node(element)
        for connections in self.connections:
            src, dest = connections
            self.graph.add_edge(src, dest)
    # think about this a litlte bit more. 
    def purpose_creation(self, simplistic_prompt, client = client):
        system_message = ""
        specifier_prompt = client.chat.completions.create(
            model="gpt-3.5-turbo",
            
            messages=[
                {"role": "system", "content": f"{system_message}"},
                {"role": "user", "content": f"""These are the elements of the system: {self.elements}. 
                                These are the connections between the elements: {self.connections}.
                                This is the purpose of the system: {self.purpose}
                                You are modeling a system. In your system you are supposed to draw the connections between your purpose, elments, and interactions. 
                                Particularly, this is what your syste is 
                                """}
                ]
        )
        
        agent_description = specifier_prompt.choices[0].message.content
        return agent_description
        
    
    
    def visualizing(self): 
        pass
    
    def creation(self):
        if self.purpose == "Archetype": # This is particularly for the archetype simulation, in which we are putting the agents into a system that is already on a bad path
            pass
        
        elif self.purpose == "System": # this is for "normal" system simulations
            pass
