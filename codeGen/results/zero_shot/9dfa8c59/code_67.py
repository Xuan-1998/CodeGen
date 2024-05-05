python
import sys

# Read input from standard input
n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations(n):
    permutations = set()
    def permute(digits):
        if len(digits) == 1:
            permutation = int(''.join(map(str, digits)))
            if is_prime(permutation):
                permutations.add(permutation)
        else:
            for i in range(len(digits)):
                remaining_digits = digits[:i] + digits[i+1:]
                permute(remaining_digits + [digits[i]])
    digits = list(map(int, str(n)))
    permute(digits)
    return len(permutations)

count = 0
smallest = float('inf')
largest = 0

for i in range(2, n_max):
    if prime_permutations(i) == k_perms:
        count += 1
        smallest = min(smallest, i)
        largest = max(largest, i)

print([count, smallest, largest])
