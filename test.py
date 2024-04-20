# import numpy as np
# import pandas as pd

# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt
# # Number of agents
# n_agents = 100

# # Generate random data for characteristics
# np.random.seed(0)
# # ages = np.random.randint(18, 65, n_agents)
# incomes = np.random.normal(50000, 15000, n_agents)
# skills = np.random.normal(5, 2, n_agents)
# preferences = np.random.rand(n_agents, 3)  # 5 different preferences

# # Create a DataFrame
# data = pd.DataFrame({
#     'Income': incomes,
#     'Skill Level': skills,
#     'Preference 1': preferences[:, 0],
#     'Preference 2': preferences[:, 1],
#     'Preference 3': preferences[:, 2]
# })

# print(data.head())

# # PCA to reduce dimensions to 2
# pca = PCA(n_components=3)
# data_pca = pca.fit_transform(data)

# # Plot
# plt.figure(figsize=(10, 6))
# plt.scatter(data_pca[:, 0], data_pca[:, 1])
# plt.title('PCA of Agent Characteristics')
# plt.xlabel('Principal Component 1')
# plt.ylabel('Principal Component 2')
# plt.grid(True)
# plt.show()

# import random 
# import numpy as np
# print(random.uniform(0,1))