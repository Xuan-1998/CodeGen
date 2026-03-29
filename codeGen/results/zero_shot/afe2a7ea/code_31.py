import math

def read_input():
    n = int(input())
    return n

n = read_input()

# Step 1: Find the number of ways to set signal powers such that towns 1 to n get signal from exactly one tower each
signal_powers_ways = 1
for i in range(2, n + 1):
    signal_powers_ways *= i

# Step 2: Find the number of ways to build radio towers and set signal powers for each town
tower_powers_ways = math.factorial(n) // (math.factorial(2) * signal_powers_ways)

print(tower_powers_ways % 998244353)
