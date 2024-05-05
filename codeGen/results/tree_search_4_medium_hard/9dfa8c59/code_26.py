from collections import defaultdict

def solve():
    n_max, k_perms = map(int, input().split())
    primes = set()
    for i in range(2, n_max+1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)

    dp = [False] * (n_max+1)
    prime_permutations = defaultdict(int)
    for p in primes:
        perms = set()
        num_str = str(p)
        for i in range(len(num_str)):
            new_num_str = ''.join(sorted(num_str[:i] + num_str[i+1:]))
            if int(new_num_str) in primes and prime_permutations[new_num_str] < k_perms:
                perms.add(int(new_num_str))
        dp[p] = len(perms) == k_perms
        for perm in perms:
            prime_permutations[str(perm)] += 1

    count = sum(1 for p in primes if dp[p])
    smallest, largest = float('inf'), -float('inf')
    for p in primes:
        if dp[p]:
            smallest, largest = min(p, smallest), max(p, largest)

    print([count, smallest, largest])

if __name__ == "__main__":
    solve()
