import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim, learning_rate=0.01):
        super(PolicyNetwork, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)  # Applying softmax on the last dimension to get probabilities
        )
        self.optimizer = optim.Adam(self.parameters(), lr=learning_rate)

    def forward(self, state):
        return self.model(state)
    
    def predict(self, state):
        state = torch.tensor(state, dtype=torch.float32).unsqueeze(0)  # Add batch dimension
        actions = self.forward(state)
        print(actions.shape)
        return actions.detach().numpy().flatten()  # Return the probability distribution as a numpy array
    
    def update(self, states, actions, rewards, next_states):
        self.optimizer.zero_grad()
        states = torch.tensor(states, dtype=torch.float32)
        actions = torch.tensor(actions, dtype=torch.long)
        rewards = torch.tensor(rewards, dtype=torch.float32)

        probs = self.forward(states)  # Get action probabilities
        action_probs = probs.gather(1, actions.unsqueeze(1)).squeeze(1)  # Get the probabilities for the taken actions
        log_probs = torch.log(action_probs)

        loss = -torch.mean(log_probs * rewards)  # Compute the loss

        loss.backward()  # Compute gradients
        self.optimizer.step()  # Update model weights
