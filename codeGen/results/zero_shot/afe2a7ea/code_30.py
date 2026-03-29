import math
p = 998244353

def calculate_probability(n):
    # Calculate the number of valid configurations for each town
    valid_configurations = [1] * (n + 2)
    
    for i in range(2, n+2):
        valid_configurations[i] = (valid_configurations[i-1] + valid_configurations[i-2]) % p
    
    # Calculate the probability that a given configuration is valid
    total_configurations = math.pow(2, n)  # 2^n possible configurations for each town
    probability = math.prod([config / total_configurations for config in valid_configurations])
    
    return int(probability)
