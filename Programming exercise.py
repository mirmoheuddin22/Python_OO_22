#Q-01:
#a)	An efficient function (Python) generating random sequence:
import random
def generate_sequence(n):
     sequence = []
     for i in range(n):
         if random.random() < 0.5:
             sequence.append("H")
         else:
             sequence.append("T")
     return sequence
print(generate_sequence(20))

#b)	An efficient function computing the length of the longest run of heads:
def longest_run(sequence):
   longest_run = 0
   current_run = 0
   for coin in sequence:
     if coin == "H":
       current_run += 1
       longest_run = max(longest_run, current_run)
     else:
       current_run = 0
   return longest_run
print(longest_run(["H", "H", "T", "H", "T", "T", "H", "H", "H", "H", "T", "T", "T", "H", "H", "T", "T", "T", "T", "H"]))

#Q-02:
#a)	Providing an efficient program code (Python) which calculates expected shortfall for this portfolio and the contribution for each of the equity positions:
import numpy as np
def expected_shortfall(returns, alpha):
    #Sorting returns in descending order
    returns.sort(reverse=True)
    #Calculating the expected shortfall at the alpha quantile
    index = int(alpha * len(returns))
    ES = np.mean(returns[index:])
    #Calculating the contribution of each equity position
    contributions = []
    for r in returns:
        if r >= ES:
            contributions.append(0)
        else:
            contributions.append(ES - r)
    return ES, contributions
returns = [0.05, 0.02, -0.03, -0.01, -0.05, -0.07]
alpha = 0.05
ES, contributions = expected_shortfall(returns, alpha)
print("Expected Shortfall:", ES)
print("Contribution of each equity position:", contributions)
