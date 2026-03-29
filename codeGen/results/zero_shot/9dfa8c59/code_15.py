import itertools

def get_prime_perms(num):
    # Convert num to a string and get all possible permutations
    perms = list(itertools.permutations(str(num)))
    
    # Filter out non-prime permutations
    prime_perms = [int(''.join(map(str, perm))) for perm in perms if is_prime(int(''.join(map(str, perm))))]
    
    return prime_perms
