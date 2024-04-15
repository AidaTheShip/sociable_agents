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
        self.purpose = purpose # this is given here.
        
    def initialize_network(self): 
        self.graph = nx.Graph()
        for element in self.elements: 
            self.graph.add_node(element)
        for connections in self.connections:
            src, dest = connections
            self.graph.add_edge(src, dest)
            
    
    def visualizing(self): 
        pass
    
    def creation(self):
        if self.purpose == "Archetype": # This is particularly for the archetype simulation, in which we are putting the agents into a system that is already on a bad path
            pass
        
        elif self.purpose == "System": # this is for "normal" system simulations
            pass
    
# # This will be relevant later. 
# def generate_convo_context(name, preference, conversation_topic, characteristics=None): 
#     agent_description_system_message = "You "
#     if characteristics is None: 
#         pass
    
#     specifier_prompt = client.chat.completions.create(
#         model="gpt-3.5-turbo",
        
#         messages=[
#             {"role": "system", "content": f"{agent_description_system_message}"},
#             {"role": "user", "content": f"""Here is what you talk about: {conversation_topic}. 
#                             Please reply with a description of {name} in {word_limit} words or less.
#                             {name} has the movie preferences in this order: {preference}. These are the only movies in discussion.
#                             Do not add anything else."""}
#             ]
#     )
    
#     agent_description = specifier_prompt.choices[0].message.content
#     return agent_description