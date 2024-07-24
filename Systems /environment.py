import random 
from tqdm import trange
import matplotlib.pyplot as plt 
import torch.nn as nn 
import torch 
import torch.nn.functional as F # contains useful functions, such as convolutions
from policynetwork import PolicyNetwork
from agent import Agent
ACTIONS = {
    "Wait": 0, # Do not deplete the resource
    "Take": 1 # Deplete the resource
}

# instantiating an environment class that defines the constraints of the simulation
class Environment:
    def __init__(self, num_agents, initial_resources) -> None:
        self.agents = [Agent(i) for i in range(num_agents)] # initiating all the agents in the simulation
        self.resources_pool = { # initiating the resource that we have, for now this will be a number
            'resources': initial_resources
        }
        self.initial_resources = initial_resources
        
    def step(self): # this is for advancing the simulation by a step
        for agent in self.agents:
            agent.choice(self.resources_pool)
        # for agent in self.agents:
        #     agent.update_policy() # Making sure that we update each agent 
    
    def run_simulation(self, episodes, steps): # this is running the entire simulation for x numebr of steps
        resource_level = []
        wealth_levels = {agent.id: [] for agent in self.agents}
        episode_rewards = []
        for _ in trange(episodes):
            self.reset()
            # resource_level = self.initial_resources
            wealth_levels = {agent.id:[] for agent in self.agents}
            for _ in range(steps):
                self.step()
                for agent in self.agents:
                    agent.update_policy()
                resource_level.append(self.resources_pool['resources'])
                for agent in self.agents:
                    wealth_levels[agent.id].append(agent.wealth)
            episode_rewards.append((resource_level, wealth_levels))
        return episode_rewards
    
    def reset(self):
        self.resources_pool = {
            'resources': self.initial_resources
        }
        for agent in self.agents:
            agent.reset()
            
    def evaluate_policy(self, steps):
        self.reset()
        resource_level = []
        wealth_levels = {agent.id: [] for agent in self.agents}
        
        for _ in trange(steps):
            self.step()
            resource_level.append(self.resources_pool['resources'])
            for agent in self.agents:
                wealth_levels[agent.id].append(agent.wealth)
        
        return resource_level, wealth_levels