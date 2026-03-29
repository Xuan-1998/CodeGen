import math

# Read input from stdin
n_max, k_perms = map(int, input().split())

count = 0
smallest_prime = float('inf')
largest_prime = -float('inf')

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_permutations(n):
    # Generate all permutations of the digits in n
    digits = list(str(n))
    permutations = []
    def permute(digits, current):
        if len(current) == len(digits):
            permutations.append(int(''.join(map(str, current))))
        else:
            for i in range(len(digits)):
                permute(digits[:i] + digits[i+1:], current + [digits[i]])
    permute(digits, [])
    return permutations

for n in range(2, n_max):  # Start from 2 because prime numbers start from 2
    if is_prime(n):
        perms = get_permutations(str(n))
        if len([p for p in perms if is_prime(p)]) == k_perms:
            count += 1
            smallest_prime = min(smallest_prime, n)
            largest_prime = max(largest_prime, n)

# Print the output to stdout
print([count, smallest_prime, largest_prime])
