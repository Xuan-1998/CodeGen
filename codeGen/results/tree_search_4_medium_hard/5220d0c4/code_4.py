import math

# Function to calculate the minimum prime divisor of an integer
def min_prime_divisor(n):
    if n < 2:
        return None
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

# Memoization dictionary to store the beauty values
memo = {}

def beauty_values(i, j, flag):
    # If the state is already computed, return the stored value
    key = (i, j, flag)
    if key in memo:
        return memo[key]
    
    # Initialize the beauty value for this subproblem
    k = 0
    
    # Iterate over the array elements and calculate the beauty value
    for p in range(2, i + 1):
        if min_prime_divisor(p) == flag: 
            k += p
        else:
            break
    
    # Store the computed beauty value and return it
    memo[key] = k
    return k

def max_beauty(n, bad_primes):
    # Initialize the maximum beauty value to 0
    max_k = 0
    
    # Iterate over the array elements and calculate the maximum beauty value
    for i in range(1, n + 1):
        for flag in [True, False]:
            k = 0
            j = 0
            while j < len(bad_primes) and bad_primes[j] <= i:
                if min_prime_divisor(i) == flag: 
                    k += i
                else:
                    break
                j += 1
            max_k = max(max_k, beauty_values(i, j, flag))
    
    return max_k

# Read input from standard input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Calculate and print the maximum beauty value
print(max_beauty(n, bad_primes))
