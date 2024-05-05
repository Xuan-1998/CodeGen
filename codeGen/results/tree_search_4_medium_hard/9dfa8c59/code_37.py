import sys

def count_prime_numbers(k_perms):
    n_max, k_perms = map(int, sys.stdin.readline().split())
    primes = set()
    for i in range(2, n_max+1):
        if all(i % j > 0 for j in range(2, int(i**0.5) + 1)):
            primes.add(i)

    dp = [[0] * (k_perms + 1) for _ in range(n_max + 1)]
    for i in range(2, n_max+1):
        if i not in primes:
            continue
        for j in range(k_perms + 1):
            if j == 0 or len(str(i)) != j:
                dp[i][j] = 0
            else:
                next_perm = get_next_prime_perm(i)
                if next_perm is None or k_perms < j:
                    dp[i][j] = dp[get_smallest_prime(i)][k_perms - 1]
                elif next_perm in primes and dp[next_perm][j-1]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

    count, smallest, largest = 0, float('inf'), float('-inf')
    for i in range(2, n_max+1):
        if i not in primes:
            continue
        if dp[i][k_perms]:
            count += 1
            smallest = min(smallest, i)
            largest = max(largest, i)

    return [count, smallest, largest]

def get_next_prime_perm(i):
    # Implement SJT or "next permutation" algorithm to generate the next prime number's permutations
    pass

print(count_prime_numbers(int(sys.stdin.readline())))
