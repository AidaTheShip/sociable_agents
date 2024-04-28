import random 
import numpy as np 
import tensorflow
from keras import layers
from agentdesign import Agent
from Networks.network import SocialNetwork

# ---------------- SETTING UP VARIABLES -------------
num_agents = 5
num_epochs = 10000 # 10000 epochs for now

# ---------------- SETTING UP HELPER FUNCTIONS -----------
def setup(agent_number, agents={}):
    
    with open('Agent_Information/information.txt', 'r') as f:
        content = f.readlines()
        content_names = [name.replace('\n', '') for name in content]
    names = np.array([random.choice(content_names) for _ in range(agent_number)])
    
    # Setting up a general environment.
    environment = SocialNetwork(names)

    # Instantiating the different agents.
    for name in names:
        agents[name] = Agent(name, environment)
        
    return environment, agents # this is returning a dictionary


environment, agents = setup(num_agents) # this automatically creates 5 agents that are randomized based on their names

# ------------ REINFORCEMENT LEARNING ------------

# # Training the agents
# def train_agents(agents, environment, num_epochs): 
#     for epoch in range(num_epochs):
#         # Resetting the environment at the start of each episode
#         current_state = environment.reset()
        
#         # Episode loop
#         done = False
#         while not done:
#             actions = {}
#             for name, agent in agents.items()


# def train_agents(agents, environment, num_epochs):
#     for epoch in range(num_epochs):
#         # Reset environment at the start of each episode
#         current_state = environment.reset()
        
#         # Episode loop
#         done = False
#         while not done:
#             actions = {}
#             for name, agent in agents.items():
#                 # Agents pick actions based on current state
#                 actions[name] = agent.decide_action(current_state)
            
#             # Update environment based on actions
#             next_state, rewards, done = environment.step(actions)
            
#             # Update agents with rewards and next state
#             for name, reward in rewards.items():
#                 agents[name].update_policy(current_state, actions[name], reward, next_state)
            
#             # Move to the next state
#             current_state = next_state

#         if epoch % 100 == 0:  # Log progress every 100 epochs
#             print(f"Epoch {epoch}: Monitoring performance...")

# # Call the training function
# train_agents(agents, environment, num_epochs)



