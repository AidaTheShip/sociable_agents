import random 
from tqdm import trange
import matplotlib.pyplot as plt 

# Let's define the base class for the agents that are going to be part of the simulation
class Agent: 
    def __init__(self, id) -> None:
        self.id = id # each of them has an id
        self.wealth = 0 # each of them has their own wealth associated with them.
        self.consumption_probability = random.uniform(0,1) # This is giving each agent a probability of depleting the resource or not depleting it
    
    def choice(self, resource_pool): 
        if random.random() < self.consumption_probability: 
            if resource_pool['resources'] > 0:
                resource_pool['resources'] -= 1
                self.wealth += 1
                return True
        return False
    
    # def consume(self, resource_pool): # this is for when the agent consumes resources durign the steps 
    #     if resource_pool['resources'] > 0: 
    #         resource_pool['resources'] -= 1
    #         self.wealth += 1

# instantiating an environment class that defines the constraints of the simulation
class Environment:
    def __init__(self, num_agents, initial_resources) -> None:
        self.agents = [Agent(i) for i in range(num_agents)] # initiating all the agents in the simulation
        self.resources_pool = { # initiating the resource that we have, for now this will be a number
            'resources': initial_resources
        }
        
    def step(self): # this is for advancing the simulation by a step
        for agent in self.agents:
            # agent.consume(self.resources_pool)
            agent.choice(self.resources_pool)
    
    def run_simulation(self, steps): # this is running the entire simulation for x numebr of steps
        resource_level = []
        wealth_levels = {agent.id: [] for agent in self.agents}
        
        for _ in trange(steps):
            self.step()
            resource_level.append(self.resources_pool['resources'])
            for agent in self.agents:
                wealth_levels[agent.id].append(agent.wealth)
        
        return resource_level, wealth_levels
    
# Let's run the simulation now. 
num_agents = 10 # number of agents we'll have in the simulation 
initial_resources = 50 # initial resources that will be exploited
steps = 50 # number of steps in the simulation

env = Environment(num_agents, initial_resources)
resource_levels, wealth_levels = env.run_simulation(steps)

# Plotting the results of the simulation 
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(resource_levels)
plt.title('Resource Levels Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Resources Left')

plt.subplot(2, 1, 2)
for agent_id, wealth in wealth_levels.items():
    plt.plot(wealth, label=f'Agent {agent_id}')
plt.title('Wealth of Each Agent Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Wealth')
plt.legend()

plt.tight_layout()
plt.show()