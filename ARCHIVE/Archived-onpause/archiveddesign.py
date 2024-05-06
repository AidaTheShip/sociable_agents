import os
import random
import numpy as np
import pandas as pd
from openai import OpenAI
# from autogen import ConversableAgent
from network import SocialNetwork
from api_keys import open_ai_key
os.environ['OPENAI_API_KEY'] = open_ai_key

client = OpenAI()

global word_limit  
word_limit = 100
global description_limit
description_limit = 50

global columns 
columns = ['Name', 'Characteristics'] # What we want to store in csv file.
db_directory = 'AgentDB'

if not os.path.exists(db_directory): # this is for making a new data base directory
    os.makedirs(db_directory)

## Intiializing the agent class
class Agent: 
    def __init__(self, name:str, directory=db_directory):
        self.name = name
        # self.characteristics = self.create_characteristics() # Puttins this on pause for a second
        self.background = self.prompt_creation()
        self.well_being = self.well_being() # encoding the well-being
#         self.agent = ConversableAgent(
#             name,
#             system_message=self.background,
#             llm_config={"config_list": [{"model": "gpt-4", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]},
#             human_input_mode="NEVER",  # Never ask for human input.
# )
        self.social_network = None
        self.characteristics = self.create_characteristics()
        self.database = pd.DataFrame(columns=columns)
        file_path = os.path.join(directory, 'agent_data.csv')
        self.database.to_csv(file_path, index=False)
                
    def prompt_creation(self):   
        specifier_prompt = client.chat.completions.create(
        model="gpt-3.5-turbo",
        
        messages=[
            {"role": "system", "content": f"Create a short description about a person with name {self.name}. Make up who they are."},
            {"role": "user", "content": f"""Tell us about what they do, what are their primary memories, what is their occupation, and what is their current state of life.
             Also, tell us their movie preferences are ranked as:. The ones that are listed last you do not like and the ones that are listed first, you do like. Own up to your preferences in conversations.
             Tell us all this in less than {description_limit} words."""}
            ]
    )
    
        description = specifier_prompt.choices[0].message.content
        
        return description
        
    def well_being(self):
        self.social_wellbeing = 0 # this will be a function based on certain characteristics of the agent + network
        self.personal_wellbeing = 0 # this will be a function based on certain characteristics of the agent
        self.purpose_wellbeing = 0 # this will be a function based on the purpose/role the agent feels they have
        
    # have to manually call this to instantiate the social network of the agent.
    def init_social_network(self, agents): 
        self.social_network = SocialNetwork(agents)
        
    
    # Challenge: How are you going to encode these characteristics? How are you going to map onto behavior?
    def create_characteristics(self):
        # What is the space of characteristics that each agent can have?
        # traits = {
        #     "Introversion": float, 
        #     "Friendliness": float, 
        #     "Conscientousness": float,
        #     "Honesty": float, 
        #     "Helpfulness": float, 
        #     "Openness": float, 
        #     "Neuroticism": float
        # }
        # num_of_characteristics = 7
        # characteristics_map = np.random.rand(7,)
        # self.characteristics = characteristics_map
        #self.introversion = random.uniform(0,1) # from 0 to 1 random number
        #self.sociality = self.social_network
        #self.well_being = self.introversion*self.sociality # much the network strength is weighted by the level of introversion
        # Mapping those onto the actual characteristics for an agent. How would you do that?
        # You could include in the prompt. How would you map it onto the prompt though? How do you make their behavior different through these characteristics?
        pass 
        
    def communicate(self):
        pass 
    
# ----------------------- CREATING AGENTS ---------------------------

def agent_creation(agent_number, agents = {}):
# For loop for instantiating x people
    with open('Agent_Information/information.txt', 'r') as f:
        content = f.readlines()
        content_names = [name.replace('\n', '') for name in content]
    # print(content_names)
    # Based on the number of agents we want, we can select random names
    names = np.array([random.choice(content_names) for _ in range(agent_number)])
    # print(type(names))
    for name in names: 
        agents[name] = Agent(name)
        agents[name].init_social_network(names) # Initializing the social network of agents by passing in all the agents that are participating in the simulation
    
    return agents

agents = agent_creation(4)
print(agents)
for agent in agents: 
    print("Agent:" + type(agent))
    agent.social_network.visualize()

# test = SocialNetwork(['a', 'b', 'c'])
# print(test.network.graph) # yay, it works!
# # a = test.network.edges('a')[0]['weight']
# for edge in test.network.edges('a'):
#     u, v = edge
#     information = test.network.get_edge_data(u, v)
#     print(information['weight'])