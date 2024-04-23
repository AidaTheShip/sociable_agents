from keras import Sequential
import tensorflow as tf
from tensorflow.keras.optimizers import Adam # why is this not being imported?
import numpy as np

### ----- THIS IS FOR OUR CUSTOM AGENT POLICY -------

class PolicyNetwork():
    # def __init__(self, curr_state) -> None:
    #     state_dim, action_dim = 1,1 # to be defined. 
    #     self.model = tf.keras.Sequential([
    #         tf.keras.layers.Dense(128, activation='relu', input_shape=(state_dim,)),
    #         tf.keras.layers.Dense(action_dim)
    #     ])
    def __init__(self, state_dim, action_dim, learning_rate=0.01):
        self.model = Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(state_dim,)),
            tf.keras.layers.Dense(action_dim)
        ])
        self.model.compile(optimizer=Adam(learning_rate), loss='mse')

    def predict(self, state):
        state = np.array(state)[np.newaxis, :]  # Expand dimensions to fit model input
        return self.model(state)
    
    def update(self, state, action, reward, next_state):
        pass

    
def update_policy(state, action, reward, new_state):
    pass