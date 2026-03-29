import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

def min_prime_divisor(x):
    if x == 1:
        return 1
    for p in range(2, int(x ** 0.5) + 1):
        while x % p == 0:
            x //= p
    return x

def is_good_prime(p):
    # Check if prime number is not in the set of bad primes
    return p not in bad_primes

def calculate_beauty(arr):
    beauty = 0
    for num in arr:
        div = min_prime_divisor(num)
        if is_good_prime(div):
            beauty += 1
    return beauty

# Calculate and print the maximum beauty of the array
max_beauty = 0
for i in range(2 ** (n - 1)):
    temp_arr = [arr[j] for j in range(n) if ((i >> j) & 1)]
    beauty = calculate_beauty(temp_arr)
    max_beauty = max(max_beauty, beauty)

print(max_beauty)
