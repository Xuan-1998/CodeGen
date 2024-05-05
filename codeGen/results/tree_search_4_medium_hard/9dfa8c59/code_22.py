from collections import defaultdict

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(num):
    if len(str(num)) == 1:  # base case: single-digit numbers don't have permutations
        return 0
    perms = set()
    for perm in itertools.permutations(str(num)):
        perms.add(int(''.join(perm)))
    return len(perms)

def solve(n_max, k_perms):
    primes = [i for i in range(2, n_max + 1) if is_prime(i)]
    state = defaultdict(int)
    
    for prime in primes:
        if count_permutations(prime) == k_perms:
            state[prime] += 1
    
    count, smallest, largest = 0, float('inf'), -float('inf')
    for prime, freq in state.items():
        count += freq
        smallest = min(smallest, prime)
        largest = max(largest, prime)
    
    return [count, smallest, largest]

if __name__ == "__main__":
    n_max, k_perms = map(int, input().split())
    print(*solve(n_max, k_perms))
