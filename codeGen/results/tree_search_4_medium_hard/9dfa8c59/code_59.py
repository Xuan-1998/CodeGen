import sys

def solve():
    n_max, k_perms = map(int, input().split())
    dp = [False] * (n_max + 1)
    count = 0
    min_prime = max_prime = 0

    for i in range(2, n_max + 1):
        if i > 1 and len(set(str(i))) == k_perms:
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
                min_prime = min(min_prime, i) if not min_prime else min_prime
                max_prime = max(max_prime, i)
        dp[i] = is_prime

    print([count, min_prime, max_prime])

if __name__ == "__main__":
    solve()
