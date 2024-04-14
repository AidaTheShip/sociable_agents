import numpy as np
ma = np.zeros((2,3))

# print(ma)
print(ma.shape)
rows, columns = ma.shape

for i in range(rows): 
    for j in range(columns): 
        print(ma[i][j])