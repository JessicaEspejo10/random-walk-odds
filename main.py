import numpy as np
import matplotlib.pyplot as plt

#setting the seed
np.random.seed(123)

#clear the plot
plt.clf()

all_walks = []
for i in range(500):
    # Initialization
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        #roll the dice
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[100,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

odd = 0
#calculate the odds
for e in ends:
    if e >= 60:
        odd += 1
odd = odd / 500
print("the probability foy you to win is about " + str(odd * 100) + "%")
