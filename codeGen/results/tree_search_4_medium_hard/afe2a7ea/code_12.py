import sys

def calculate_probability():
    n = int(sys.stdin.readline())
    mod = 998244353
    
    # Calculate the number of valid configurations
    valid_configurations = 1
    for i in range(2, n+2):
        valid_configurations *= (i-1)
    
    # Calculate the total number of configurations
    total_configurations = 2**n
    
    # Calculate the probability and print it modulo 998244353
    probability = valid_configurations * pow(total_configurations, mod-2, mod) % mod
    
    print(probability)

calculate_probability()
