import itertools

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def permutations(s):
    """Generate all possible permutations of the digits in a number"""
    s = str(s)
    return [''.join(p) for p in itertools.permutations(s)]

n_max, k_perms = map(int, input().split())
count = 0
smallest = largest = None

for i in range(2, n_max + 1):
    if is_prime(i):
        perms = permutations(str(i))
        if len([p for p in perms if int(p) < i and is_prime(int(p))]) == k_perms:
            count += 1
            smallest = largest = i

if count > 0:
    print([count, smallest, largest])
else:
    print([0, 0, 0])
