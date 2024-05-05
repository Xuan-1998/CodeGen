from math import comb
n = int(input())

# Calculate the total number of ways to choose signal powers for towers
total_ways = 1
for i in range(1, n+1):
    total_ways *= (i + 2)

# The total number of ways to set signal powers is calculated by multiplying the number of possibilities for each town.
total_ways *= comb(n, n//2) # This calculates the number of ways to choose which towns get signals from which towers.

# Calculate the number of invalid configurations. A configuration is invalid if some town gets signal from multiple towers or no town gets signal.
invalid_ways = 0
for i in range(1, n+1):
    for j in range(i+1, n+2): # Iterate over all possible combinations of towns that can get signals.
        invalid_ways += comb(n//i, j-i) * comb(n-j, j//i) # This calculates the number of ways to choose signal powers for the current configuration.

# The probability is calculated by dividing the total number of valid configurations by the total number of possible configurations and taking the modulo 998244353.
prob = (total_ways - invalid_ways) % 998244353

print(prob)
