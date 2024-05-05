import sys
def read_input():
    return int(sys.stdin.readline())

n = read_input()

# Step 1: Initialize the probability as 1 (since we know at least one way of setting signal powers)
probability = 1

# Step 2: Calculate the number of ways to set signal powers for each town.
for i in range(1, n+1):
    # For each town, we have (n-i) choices for which tower's signal power to take
    probability *= (n-i)

# Step 3: Use the fact that the total number of ways to set signal powers is 2^n, and divide it by the calculated probability.
probability = pow(2, n, 998244353) // probability

print(probability)
