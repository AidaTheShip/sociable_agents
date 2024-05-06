import torch 
import torch.nn
from network import SocialNetwork
from agentdesign import Agent
import matplotlib.pyplot as plt
import networkx as nx

# Setup function for agents and network
def setup(num_agents):
    agent_names = [f"Agent_{i}" for i in range(num_agents)]
    network = SocialNetwork(agent_names)
    agents = {name: Agent(name, network) for name in agent_names}
    return agents, network

# Training function
def train(agents, network, num_episodes, max_steps_per_episode):
    rewards_history = []

    for episode in range(num_episodes):
        total_reward = 0

        for step in range(max_steps_per_episode):
            for agent in agents.values():
                old_state, action, next_state, reward = agent.action()
                agent.policy_net.update(torch.tensor([old_state], dtype=torch.float32),
                                        torch.tensor([action], dtype=torch.int64),
                                        torch.tensor([reward], dtype=torch.float32),
                                        torch.tensor([next_state], dtype=torch.float32))
                total_reward += reward

        rewards_history.append(total_reward)
        print(f"Episode {episode + 1}: Total Reward = {total_reward}")

    plt.plot(rewards_history)
    plt.title('Total Rewards per Episode')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.show()

# Assuming we have 5 agents
agents, network = setup(5)
train(agents, network, 100, 100)
