import networkx as nx
from network import SocialNetwork
import numpy as np
import random
from agentdesign import Agent
import os



# ---------------- HELPER FUNCTIONS FOR SETUP ------------------
def setup(num_agents, agents={}):
    try:
        with open('Agent_Information/information.txt', 'r') as f:
            content = f.readlines()
        content_names = [name.strip() for name in content]  # Using strip() to remove any leading/trailing whitespace

        if content_names:  # Check if the list is not empty
            names = np.array([random.choice(content_names) for _ in range(num_agents)])
            # print(names)
        else:
            print("No names are available in the file.")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Create general social network based on the agents
    network = SocialNetwork(names) # this is instantiating a network with all the agents that will be in the simulation but with no connection initially.
    # Create each agent with the knowledge of the social network
    for name in names:
        agents[name] = Agent(name, network)
    return agents, network

participants, network = setup(3)

# ------------- REINFORCEMENT LEARNING ---------------
num_episodes = 1000
max_steps_per_episode = 100
timestep = 1 # at every time step each agent can make a decision in the environment

# Storing the development of our data.
columns = ['Name', 'Characteristics'] # What we want to store in csv file.
db_directory = 'AgentDB'

if not os.path.exists(db_directory): # this is for making a new data base directory
    os.makedirs(db_directory)

class Environment():
    def __init__(self, agent, agents, social_network):
        self.agents = agents
        self.agent = agent
        self.inital_social_network = agent.social_network
        self.social_network = agent.social_network
        
    def step(self, agent, action):
        
        old_sn = self.social_network
        
        old_state, action, new_state, reward = self.agent.perform_action(action) # note that we are already updating hte policy network in this agent function. As well as the network itself. 
        
        new_sn = self.agent.social_network
        # Updating and Storign the states, showcasing the change in the social network
        
        return new_state, reward
    
    def reset(self):
        # Resetting the environment for each time step. We do not reset the agents but we do reset the social network
        self.agent.social_network = self.inital_social_network

# ------ ACTUALLY TRAINING THE AGENTS -------
def training(agents: list[Agent], social_network, num_episodes, max_steps_per_episode):
    env = Environment(agents, social_network)
    # SET UP STRUCTURES FOR STORING THE DATA HERE
    
    for episode in range(num_episodes):
        state = env.reset()
        for step in range(max_steps_per_episode):
            old_state = [agent.get_state() for agent in agents]
            actions = [agent.decide_action() for agent in agents]
            rewards = []
            
            for agent in agents: 
                next_state, reward = env.step(agent, agent, actions)
                rewards.append(reward)
                for name, agent in agents.items():
                    agent.update_policy(state[name], actions[name], rewards[name], next_state[name])
                state = next_state
    
    # while True:
    #     # get the old state
    #     old_state = agent.get_state()
    #     # Decide for an action to take
    #     action = agent.decide_action()
        
    #     # Taking a step for environment
    #     env.step(agent, action)


            

# # def training_agents(num_episodes, max_steps_per_episode):
# #     for episode in range(num_episodes):
# #         state = None # RESETTING THE ENVIRONMENT. THINK ABOUT WHAT THIS MEANS. ENV.RESET() => WHAT???
# #         for step in range(max_steps_per_episode):
            
            
# # for episode in range(num_episodes):
# #     state = env.reset()
# #     for step in range(max_steps_per_episode):
# #         actions = [agent.select_action(state[agent_id]) for agent_id, agent in enumerate(agents)]
# #         next_state, rewards, done, info = env.step(actions)

# #         # Example update step for REINFORCE (Policy Gradient)
# #         for agent_id, agent in enumerate(agents):
# #             agent.update_policy(rewards[agent_id], optimizers[agent_id])

# #         state = next_state
# #         if done:
# #             break

# #     # Optionally log progress here

# # # Testing loop
# # for episode in range(100):  # 100 testing episodes
# #     state = env.reset()
# #     for step in range(max_steps_per_episode):
# #         actions = [agent.select_action(state[agent_id], explore=False) for agent_id, agent in enumerate(agents)]
# #         next_state, rewards, done, info = env.step(actions)
# #         state = next_state
# #         if done:
# #             break




# # # ------------- [ARCHIVE] TESTING IMPORTS -------------
# # # # print(participants)
# # # print(participants, network)
# # # print(network.network.edges)

# # # test = SocialNetwork(['a', 'b', 'c'])
# # # print(test.network.edges)