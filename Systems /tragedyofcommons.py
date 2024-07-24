import random 
from tqdm import trange
import matplotlib.pyplot as plt 
import torch.nn as nn 
import torch 
import torch.nn.functional as F # contains useful functions, such as convolutions
from policynetwork import PolicyNetwork
from agent import Agent
from environment import Environment

ACTIONS = {
    "Wait": 0, # Do not deplete the resource
    "Take": 1 # Deplete the resource
}

# Let's run the simulation now. 
num_agents = 10 # number of agents we'll have in the simulation 
initial_resources = 50 # initial resources that will be exploited
steps = 50 # number of steps in the simulation
steps_per_episode = 50
episodes = 10

env = Environment(num_agents, initial_resources)
# resource_levels, wealth_levels = env.run_simulation(steps)
episode_rewards = env.run_simulation(episodes, steps_per_episode)

plt.figure(figsize=(12, 6))

for episode, (resource_levels, wealth_levels) in enumerate(episode_rewards):
    plt.subplot(episodes, 1, episode + 1)
    plt.plot(resource_levels, label='Resources')
    for agent_id, wealth in wealth_levels.items():
        plt.plot(wealth, label=f'Agent {agent_id}')
    plt.title(f'Episode {episode + 1}')
    plt.xlabel('Time Steps')
    plt.ylabel('Value')
    plt.legend()

plt.tight_layout()
plt.show()

# # Plotting the results of the simulation 
# plt.figure(figsize=(12, 6))
# plt.subplot(2, 1, 1)
# plt.plot(resource_levels)
# plt.title('Resource Levels Over Time')
# plt.xlabel('Time Steps')
# plt.ylabel('Resources Left')

# plt.subplot(2, 1, 2)
# for agent_id, wealth in wealth_levels.items():
#     plt.plot(wealth, label=f'Agent {agent_id}')
# plt.title('Wealth of Each Agent Over Time')
# plt.xlabel('Time Steps')
# plt.ylabel('Wealth')
# plt.legend()

# plt.tight_layout()
# plt.show()
