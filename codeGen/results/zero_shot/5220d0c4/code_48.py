# Read the input from stdin
n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Initialize maximum beauty as 0
max_beauty = 0

# Iterate over each number in the array
for num in array:
    # Check if the number is a prime number (good or bad)
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # If it's a good prime, increment the beauty by the number itself
    if is_prime and num not in bad_primes:
        max_beauty += num
    
    # If it's a bad prime, decrement the beauty by 1
    elif is_prime and num in bad_primes:
        max_beauty -= 1

# Print the maximum beauty to stdout
print(max_beauty)
