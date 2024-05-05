### BEGIN SOLUTION
import itertools

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def permutations(digits):
    """Generate all possible permutations of digits."""
    return list(itertools.permutations(map(int, str(digits))))

def count_prime_permutations(num):
    """Count the number of prime permutations for a given number."""
    perms = set(permutations(num))
    return sum(1 for p in perms if is_prime(int(''.join(map(str, p)))))

n_max, k_perms = map(int, input().split())
count, smallest, largest = 0, float('inf'), -float('inf')

for num in range(2, n_max + 1):
    if is_prime(num) and count_prime_permutations(num) == k_perms:
        count += 1
        smallest = min(smallest, num)
        largest = max(largest, num)

print(count, smallest, largest)
### END SOLUTION
