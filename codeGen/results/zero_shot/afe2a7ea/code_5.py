import sys

# Define the modulo value
MOD = 998244353

def find_signal_powers(n):
    # Calculate the number of ways to order the towns that don't receive a signal
    permutations = 2 ** (n + 1)
    
    # Initialize the result as 0
    total_permutations = 0
    
    for _ in range(permutations):
        # For each permutation, calculate the number of ways to assign signal powers
        power_assignments = 1
        
        for i in range(1, n + 2):
            if not (i % 2):  # If this is an even town that doesn't receive a signal
                power_assignments *= (n - i)  # There are n-i ways to assign a unique signal
            else:  # If this is an odd town that receives a signal
                power_assignments *= i  # There are i ways to assign the current signal
        
        total_permutations += power_assignments
    
    return total_permutations % MOD

n = int(sys.stdin.readline())
print(find_signal_powers(n))
