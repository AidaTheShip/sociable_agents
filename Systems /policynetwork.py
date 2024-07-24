import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim, learning_rate=0.01, gamma=0.9):
        super(PolicyNetwork, self).__init__()
        hidden_layer = 128
        self.model = nn.Sequential( # creating a neural network structure here
            nn.Linear(state_dim, hidden_layer),
            nn.ReLU(), 
            nn.Linear(hidden_layer, action_dim),
            nn.Softmax(dim=-1)
        )
        self.optimizer = optim.Adam(self.parameters(), lr=learning_rate)
        self.gamma = gamma

    def forward(self, state):
        # state = state.clone().detach().requires_grad_(True)  # Add batch dimension
        return self.model(state) # returning action based on the input, which in our case will be the state.
    
    def update(self, rewards, log_probs):
        rewards = torch.tensor(rewards, dtype=torch.float32)

        # Calculate policy loss
        policy_loss = []
        for log_prob, reward in zip(log_probs, rewards):
            policy_loss.append(-log_prob * reward)
        
        if policy_loss:
            policy_loss = torch.stack(policy_loss).sum()
        else:
            print("Policy loss list is empty.")
            return None

        # Perform backpropagation
        self.optimizer.zero_grad()
        policy_loss.backward()
        self.optimizer.step()

        return policy_loss
