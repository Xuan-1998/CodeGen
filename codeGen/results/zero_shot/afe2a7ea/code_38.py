import math

def solve():
    n = int(input())
    
    # Initialize an empty list for signal powers
    signal_powers = [0] * (n + 1)
    
    # Calculate the total number of ways to set signal powers
    total_ways = 1
    for i in range(2, n + 1):
        total_ways *= i
    
    # Calculate the number of ways that satisfy all constraints
    constrained_ways = 1
    for i in range(2, n):
        constrained_ways *= (n - i)
    
    # Calculate the probability
    prob = constrained_ways * pow(total_ways, -1, 998244353)
    
    print(int(prob))
