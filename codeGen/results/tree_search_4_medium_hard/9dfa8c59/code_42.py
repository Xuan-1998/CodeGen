from collections import defaultdict

def prime_permutations(n_max, k_perms):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = set()
    for i in range(2, n_max + 1):
        if is_prime(i):
            primes.add(i)

    prime_perm_counts = defaultdict(int)
    for p in primes:
        perm_count = 0
        p_str = str(p)
        for _ in range(len(p_str)):
            for c in set(p_str):
                new_p_str = ''.join(sorted([c] + [d for d in p_str if d != c]))
                new_p = int(new_p_str)
                if is_prime(new_p) and new_p < n_max:
                    perm_count += 1
        prime_perm_counts[perm_count] += 1

    count = 0
    smallest = largest = 0
    for k, v in prime_perm_counts.items():
    # Filter the counts based on the condition: k == k_perms
    if k == k_perms:
        count += v
        if not smallest:
            smallest = min(primes.intersection(range(n_max)))
        largest = max((primes & range(n_max)).intersection(prime_perm_counts[k]))
    return [count, smallest, largest]

n_max, k_perms = map(int, input().split())
print(prime_permutations(n_max, k_perms))
