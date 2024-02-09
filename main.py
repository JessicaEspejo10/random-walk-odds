import numpy as np

#setting the seed
np.random.seed(123)

#starting step
step = 0

#roll the dice
dice = np.random.randint(1,7)

#control construct
if dice <= 2 :
    step = step - 1
elif dice <6 :
    step =+ 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print("dice: " + str(dice) + " - Step: " + str(step))
