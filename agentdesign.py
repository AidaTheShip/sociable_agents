import os
import random
import numpy as np
from openai import OpenAI
from autogen import ConversableAgent

from api_keys import open_ai_key
os.environ['OPENAI_API_KEY'] = open_ai_key

client = OpenAI()

global word_limit  
word_limit = 100
global description_limit
description_limit = 50

# BASIC VARIABLES (we'll eventually put these into)
# movies = ["Avatar", "Avengers", "Titanic", "Jurassic World", "Star Wars"]

## Intiializing the agent class
class Agent: 
    def __init__(self, name:str):
        self.name = name
        self.movie_preferences = self.create_movie_preferences()
        # self.characteristics = self.create_characteristics() # Puttins this on pause for a second
        self.background = self.prompt_creation()
        self.well_being = self.well_being() # encoding the well-being
        self.agent = ConversableAgent(
            name,
            system_message=self.background,
            llm_config={"config_list": [{"model": "gpt-4", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]},
            human_input_mode="NEVER",  # Never ask for human input.
)
        self.characteristics = self.characteristics()
        
    def prompt_creation(self):   
        specifier_prompt = client.chat.completions.create(
        model="gpt-3.5-turbo",
        
        messages=[
            {"role": "system", "content": f"Create a short description about a person with name {self.name}. Make up who they are."},
            {"role": "user", "content": f"""Tell us about what they do, what are their primary memories, what is their occupation, and what is their current state of life.
             Also, tell us their movie preferences are ranked as: {self.movie_preferences}. The ones that are listed last you do not like and the ones that are listed first, you do like. Own up to your preferences in conversations.
             Tell us all this in less than {description_limit} words."""}
            ]
    )
    
        description = specifier_prompt.choices[0].message.content
        return description
        
    def well_being(self):
        self.social_wellbeing = 0 # this will be a function based on certain characteristics of the agent + network
        self.personal_wellbeing = 0 # this will be a function based on certain characteristics of the agent
        self.purpose_wellbeing = 0 # this will be a function based on the purpose/role the agent feels they have
        
    def social_network(self): 
        pass
    
    def create_movie_preferences(self, movies=movies): 
        return random.sample(movies, len(movies))
    
    def characteristics(self):
        # What is the space of characteristics that each agent can have?
        traits = {
            "Introversion": float, 
            "Friendliness": float, 
            "Conscientousness": float,
            "Honesty": float, 
            "Helpfulness": float, 
            "Openness": float, 
            "Neuroticism": float
        }
        
        
        # Mapping those onto the actual characteristics for an agent. How would you do that?
        # You could include in the prompt. How would you map it onto the prompt though? How do you make their behavior different through these characteristics?
        # TO-DO
        
        return traits

def generate_convo_context(name, preference, conversation_topic, characteristics=None): 
    agent_description_system_message = "You "
    if characteristics is None: 
        pass
    
    specifier_prompt = client.chat.completions.create(
        model="gpt-3.5-turbo",
        
        messages=[
            {"role": "system", "content": f"{agent_description_system_message}"},
            {"role": "user", "content": f"""Here is what you talk about: {conversation_topic}. 
                            Please reply with a description of {name} in {word_limit} words or less.
                            {name} has the movie preferences in this order: {preference}. These are the only movies in discussion.
                            Do not add anything else."""}
            ]
    )
    
    agent_description = specifier_prompt.choices[0].message.content
    return agent_description