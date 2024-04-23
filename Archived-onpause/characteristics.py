import numpy as np 


# traits = {
#             "Introversion": float, 
#             "Friendliness": float, 
#             "Conscientousness": float,
#             "Honesty": float, 
#             "Helpfulness": float, 
#             "Openness": float, 
#             "Neuroticism": float
#         }
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Number of agents
n_agents = 5

# Traits
traits = ["Introversion", "Friendliness", "Conscientiousness", "Honesty", "Helpfulness", "Openness", "Neuroticism"]

# Initialize random traits for each agent
agents_traits = np.random.rand(n_agents, len(traits))

# Create a DataFrame for better handling in seaborn
df_agents = pd.DataFrame(agents_traits, columns=traits)

# Create a pair plot
sns.pairplot(df_agents)
plt.suptitle('Pair Plot of Agent Traits', y=1.02)  # Adjust the title position
plt.show()
