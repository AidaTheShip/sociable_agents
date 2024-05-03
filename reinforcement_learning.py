import random 
import numpy as np 
import tensorflow
from keras import layers
from agentdesign import Agent
from network import SocialNetwork 

# ---------------- SETTING UP VARIABLES -------------
num_agents = 5
num_epochs = 10000 # 10000 epochs for now

print("Hello world")
# ---------------- SETTING UP HELPER FUNCTIONS -----------


def setup(agent_number, agents={}):
    
    with open('Agent_Information/information.txt', 'r') as f:
        content = f.readlines()
        content_names = [name.replace('\n', '') for name in content]
    names = np.array([random.choice(content_names) for _ in range(agent_number)])
    
    # Setting up a general environment.
    # environment = SocialNetwork(names)
    print(names)
    print(environment)
    # Instantiating the different agents.
    for name in names:
        agents[name] = Agent(name, environment)
    
    return environment, agents # this is returning a dictionary


environment, agents = setup(num_agents) # this automatically creates 5 agents that are randomized based on their names

# ------------ REINFORCEMENT LEARNING ------------

for agent in agents: 
    print(agent)

# Training the agents
def train_agents(agents, environment, num_epochs): 
    for epoch in range(num_epochs):
        # Resetting the environment at the start of each episode
        env_state = environment.reset()
        
        # Episode loop
        done = False
        while not done:
            actions = {}
            states = {}
            rewards = {}
            for name, agent in agents.items(): # agents.items is a dictionary
               actions[name] = agent.decide_action() # for now, we are not going to input the environment state
               next_state, reward = agent.perform_action(actions[name]) # this is going to update the social network structure, and update the policy network already

            # Update environment based on actions            
            # Update agents with rewards and next state
            for name, reward in rewards.items():
                agents[name].update_policy(current_state, actions[name], reward, next_state)
            
            # Move to the next state
            current_state = next_state

        if epoch % 100 == 0:  # Log progress every 100 epochs
            print(f"Epoch {epoch}: Monitoring performance...")
        done = epoch > num_epochs

# Call the training function
train_agents(agents, environment, num_epochs)

