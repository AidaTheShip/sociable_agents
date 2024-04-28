from keras import Sequential
from keras.layers import Dense
import tensorflow as tf
import numpy as np
from keras.optimizers import Adam
from keras import Sequential
from keras.layers import Dense
import tensorflow as tf
import numpy as np
from keras.optimizers import Adam
from keras.losses import MeanSquaredError

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
            Dense(128, activation='relu', input_shape=(state_dim,)),
            Dense(action_dim, activation='softmax')
        ])
        self.optimizer = Adam(learning_rate)
        self.action_dim = action_dim
        
    def predict(self, state):
        # state = np.array(state)[np.newaxis, :]  # Expand dimensions to fit model input
        actions = self.model.predict(state)
        print(actions.shape)
        return actions.flatten() # just returning the Probability distribution
    
    def update(self, state, action, reward, next_state):
        with tf.GradientTape() as tape:
        # Forward pass: compute the probabilities
            state = tf.convert_to_tensor(state, dtype=tf.float32)
            probs = self.model(state, training=True)  # Get action probabilities

            # Get the log probabilities of the selected action
            action_probs = tf.gather_nd(probs, indices=[[i, action[i]] for i in range(len(action))])
            log_probs = tf.math.log(action_probs)

            # Compute loss as negative log probability times the reward
            loss = -tf.reduce_mean(log_probs * reward)

        # Compute gradients and update model weights
        gradients = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))
