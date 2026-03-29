# Step 1: Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Step 2: Define a function to check if a number is good or bad prime
def is_good_prime(n):
    # Check if the number is prime and not in the set of bad primes
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Step 3: Define a function to calculate the beauty of an array
def calculate_beauty(arr):
    beauty = 0
    for num in arr:
        # Calculate the minimum prime divisor of each number
        min_prime_divisor = None
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0 and is_good_prime(i):
                min_prime_divisor = i
                break
        # Add the beauty of this number to the total beauty
        if min_prime_divisor:
            beauty += min_prime_divisor
    return beauty

# Step 4: Calculate the maximum beauty by iterating through all possible subsets of the array
max_beauty = 0
for i in range(1 << n):
    subset = [arr[j] for j in range(n) if (i & (1 << j))]
    max_beauty = max(max_beauty, calculate_beauty(subset))

# Step 5: Print the maximum beauty
print(max_beauty)
