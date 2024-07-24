import random 
from tqdm import trange
import matplotlib.pyplot as plt 
import torch.nn as nn 
import torch 
import torch.nn.functional as F # contains useful functions, such as convolutions
from policynetwork import PolicyNetwork

ACTIONS = {
    "Wait": 0, # Do not deplete the resource
    "Take": 1 # Deplete the resource
}
# Preliminarily defining the dimensions we are working on. 
global action_dim
action_dim = 2
global state_dim
# For now, this is going to be the wealth and the overall resource pool
state_dim = 2
# STATES are continuously 2 dimensional (wealth & resource_pool)

# Let's define the base class for the agents that are going to be part of the simulation
class Agent: 
    def __init__(self, id, state_dim=state_dim, action_dim=action_dim) -> None:
        self.id = id # each of them has an id
        self.wealth = 0 # each of them has their own wealth associated with them.
        self.policy = PolicyNetwork(state_dim, action_dim) # this is the policy network we are instantiating.
        # Integrating Memory for each agent
        self.rewards = [] # Memory to store past actions and rewards
        self.log_probs = [] # logging the log probabilities of the actions 
        
    def choice(self, resource_pool): 
        # Integrating the choice in here,  # the state of the agent is the state of wealth and the resource_pool even if the agent does not realize / "feel" the resoruce pool
        state = torch.tensor([self.wealth, resource_pool['resources']], dtype=torch.float32) # this is the current state.
        action_probs = self.policy.forward(state) # this is the action probabilities as calculated by the policy
        print(f"First: {action_probs}")
        if torch.isnan(action_probs).any():
            print(f"NaN detected in action probabilities: {action_probs}")
            return ACTIONS["Wait"]  # Default action in case of NaN
        action_distribution = torch.distributions.Categorical(action_probs)
        # print(f"Action distribution {action_distribution.sample()}")
        # action = torch.argmax(action_probs).item() # takes the action that has a higher probability
        action = action_distribution.sample() # sampling one of the actions.
        self.log_probs.append(action_distribution.log_prob(action))
        
        # Integrating Reward as self.wealth for now.
        reward = 0 
        # ACTIONS["Take"] is 1
        if action == ACTIONS["Take"]:
            if resource_pool['resources'] > 0: # Checking whether there is still a resource pool
            # If resources still exist, then you can deplete it and get personal wealth out of it.
                resource_pool['resources'] -= 1
                reward = 1
            else:
                reward = -1
        # ACTIONS["Wait"] is 0
        elif action == ACTIONS['Wait']: # if the agents chooses to wait
            # potentially
            # resource_pool['resources'] += 1
            reward = 0
        
        self.wealth += reward
        self.rewards.append(reward)
        
        return action.item()
        
        # next_state = [self.wealth, resource_pool['resources']]
        # # self.memory.append([state.squeeze().tolist(), action, self.wealth, next_state])
        # # state = torch.tensor(state, dtype=torch.float64)
        # action = torch.tensor(action, dtype=torch.float32)
        # reward = torch.tensor(self.wealth, dtype=torch.float32)
        # next_state = torch.tensor(next_state, dtype=torch.float32)
        # print(state.shape)
        # # Now we update the policy network. 
        # loss = self.policy.update(state, action, reward, next_state)
        # print(loss)    
        
    def update_policy(self): 
        loss = self.policy.update(self.rewards, self.log_probs)
        self.log_probs = []
        self.rewards = []
        return loss
        
