import numpy as np
die_sides=int(input("Enter number of sides of dice(6/12):"))
die=range(1,die_sides)
num_rolls=int(input("ENter the number of times you wanna role the dice:"))
results= np.random.choice(die,size=num_rolls,replace=True)
print(results)