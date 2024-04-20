from keras import Sequential
import tensorflow as tf

### ----- THIS IS FOR OUR CUSTOM AGENT POLICY -------

class PolicyNetwork():
    def __init__(self) -> None:
        state_dim, action_dim = 1,1 # to be defined. 
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(state_dim,)),
            tf.keras.layers.Dense(action_dim)
        ])
    
    def predict(self, state):
        return self.model(state)
    
def update_policy(state, action, reward, new_state):
    pass