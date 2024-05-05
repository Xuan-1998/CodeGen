import sys

def solve(n_max, k_perms):
    # Step 1: Generate all prime numbers up to n_max using a sieve algorithm
    primes = []
    sieve = [True] * (n_max + 1)
    for p in range(2, int(n_max ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n_max + 1, p):
                sieve[i] = False
    for p in range(2, n_max + 1):
        if sieve[p]:
            primes.append(p)

    # Step 2: For each prime number p, generate its permutations and count the number of prime permutations
    prime_counts = {}
    for p in primes:
        perms = set()
        for perm in itertools.permutations(str(p)):
            num = int(''.join(perm))
            if sieve[num]:
                perms.add(num)
        if len(perms) == k_perms:
            prime_counts[p] = (len(perms), min(perms), max(perms))

    # Step 3: Return the count of prime numbers with k_perms prime permutations, the smallest, and the largest
    result = [0, float('inf'), -float('inf')]
    for p, counts in prime_counts.items():
        if counts[0] == k_perms:
            result[0] += 1
            result[1] = min(result[1], p)
            result[2] = max(result[2], p)

    return [result[0], result[1], result[2]]

if __name__ == '__main__':
    n_max, k_perms = map(int, sys.stdin.readline().split())
    print(*solve(n_max, k_perms), sep='\n')
