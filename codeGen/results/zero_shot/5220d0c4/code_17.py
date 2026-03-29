import sys

# Read input
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

# Define a function to calculate the beauty of an array
def calculate_beauty(arr):
    beauty = 0
    for num in arr:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if not is_prime or num in bad_primes:
            beauty -= min(range(2, num), key=lambda x: x if num % x == 0 else float('inf'))
        else:
            beauty += min(range(2, num), key=lambda x: x if num % x == 0 else float('inf'))
    return beauty

# Find the maximum beauty
max_beauty = calculate_beauty(arr)
print(max_beauty)
