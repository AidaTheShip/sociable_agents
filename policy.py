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
            nn.Softmax(dim=-1)
        )
        self.optimizer = optim.Adam(self.parameters(), lr=learning_rate)

    def forward(self, state):
        return self.model(state)

    def predict(self, state):
        state = torch.tensor(state, dtype=torch.float32).unsqueeze(0)  # Add batch dimension
        return self.forward(state)

    def update(self, states, actions, rewards, next_states):
        self.optimizer.zero_grad()
        current_q = self.forward(states).gather(1, actions.unsqueeze(1))
        max_next_q = self.forward(next_states).max(1)[0].detach()
        expected_q = rewards + 0.99 * max_next_q  # Assuming a discount factor of 0.99

        loss = F.mse_loss(current_q.squeeze(), expected_q)
        loss.backward()
        self.optimizer.step()

        return loss