# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Initialize maximum beauty and bad count
max_beauty = 0
bad_count = 0

# Iterate over the array
for num in arr:
    # Check if number is a bad prime
    if any(num % bad_prime == 0 for bad_prime in bad_primes):
        bad_count += 1
        continue
    
    # Find minimum prime divisor
    min_divisor = 2
    while min_divisor * min_divisor <= num:
        if num % min_divisor:
            break
        min_divisor += 1
    
    # Update maximum beauty
    max_beauty = max(max_beauty, num // min_divisor)

# Print the maximum beauty
print(max_beauty)
