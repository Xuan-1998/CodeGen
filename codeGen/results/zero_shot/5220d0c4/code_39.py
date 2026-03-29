# Read the input
n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Function to find the minimum prime divisor of a number
def min_prime_divisor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

# Function to find the beauty of an array
def array_beauty(array):
    beauty = 0
    for num in array:
        if min_prime_divisor(num) not in bad_primes:
            beauty += 1
    return beauty

# Find the maximum beauty by trying all possible subsets
max_beauty = 0
for i in range(2**n):
    subset = [array[j] for j in range(n) if (i >> j) & 1]
    max_beauty = max(max_beauty, array_beauty(subset))

# Print the maximum beauty
print(max_beauty)
