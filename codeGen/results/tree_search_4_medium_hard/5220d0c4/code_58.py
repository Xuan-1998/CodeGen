import sys
from functools import lru_cache

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find the smallest divisor of a number (used for prime checking)
def smallest_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i

# Function to calculate the beauty value
@lru_cache(maxsize=None)
def beauty(i, j, f, g):
    if i > j:
        return 0
    
    # Calculate the minimum prime divisor for the current window
    min_divisor = sys.maxsize
    for num in range(i, j+1):
        if is_prime(num) and (f == 0 or smallest_divisor(num) != smallest_divisor(g)):
            min_divisor = min(min_divisor, smallest_divisor(num))
    
    # Calculate the beauty value based on the minimum prime divisor and whether it's a good or bad prime
    return max(beauty(i, j-1, f, g), min_divisor)

# Main function to read input and print output
def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    # Initialize the memoization dictionary with base cases (i.e., empty subarrays)
    memo = {(0, j, 0, 0): 0 for j in range(n)}

    # Calculate and print the maximum beauty value
    max_beauty = 0
    for i in range(1, n):
        for f in [0, 1]:
            g = nums[i-1]
            if is_prime(g) and (f == 0 or smallest_divisor(g) != smallest_divisor(bad_primes[0])):
                max_beauty = max(max_beauty, beauty(i, i-1, f, g))
    
    print(max_beauty)

if __name__ == "__main__":
    main()
