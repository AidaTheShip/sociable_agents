import torch 
import torch.nn
from network import SocialNetwork
from agentdesign import Agent
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# ------ HELPER FUNCTIONS -------
snapshots = []
# Setup function for agents and network
def setup(num_agents, path=None):
    if not path:
        agent_names = [f"Agent{i}" for i in range(num_agents)]
    else:
        try:
            with open(path, 'r') as f:
                content = f.readlines()
                content_names = [name.strip() for name in content]
                if content_names:  # Check if the list is not empty
                    names = np.array([random.choice(content_names) for _ in range(num_agents)])
                    # print(names)
                else:
                    print("No names are available in the file.")
        except FileNotFoundError:
            print("The specified file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    network = SocialNetwork(agent_names)
    agents = {name: Agent(name, network) for name in agent_names}
    return agents, network

def visualize_network(network, title="Social Network"):
    pos = nx.spring_layout(network)
    weights = nx.get_edge_attributes(network, 'weight')
    nx.draw(network, pos, with_labels=True, node_size=700, node_color='skyblue',
            edge_color=[float(v) for v in weights.values()], width=4, edge_cmap=plt.cm.Blues)
    plt.title(title)
    plt.show()

# ------ TRAINING -----
# Training function

# Training function
def train(agents, network, num_episodes, max_steps_per_episode):
    rewards_history = {agent_name: [] for agent_name in agents.keys()}
    network_evolution = []

    for episode in trange(num_episodes):
        episode_network = {}
        if episode % 10 == 0:
            snapshots.append(network.snapshot())
        
        for agent_name, agent in agents.items():
            # print(agent_name)
            total_reward = 0
            for step in range(max_steps_per_episode):
                old_state, action, next_state, reward = agent.action()
                agent.policy_net.update(torch.tensor([old_state], dtype=torch.float32),
                                         torch.tensor([action], dtype=torch.int64),
                                         torch.tensor([reward], dtype=torch.float32),
                                         torch.tensor([next_state], dtype=torch.float32))
                total_reward += reward
            rewards_history[agent_name].append(total_reward)
            episode_network[agent_name] = np.array(agent.get_state())

        network_evolution.append(episode_network)

    df_network_evolution = pd.DataFrame(network_evolution)

    for agent_name, rewards in rewards_history.items():
        plt.plot(rewards)
        plt.title(f'Total Rewards per Episode for agent {agent_name}')
        plt.xlabel('Episode')
        plt.ylabel('Total Reward')
        plt.show()

    visualize_network(snapshots[0], "Network at Start")
    visualize_network(snapshots[-1], "Network at End")
    return rewards_history

# Assuming we have 5 agents
agents, network = setup(5)
history_rewards = train(agents, network, 100, 100)
