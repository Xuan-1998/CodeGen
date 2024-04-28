import sys

def count_permutations(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    total_counts = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if j < i and not can_sort(j, i - 1):
                continue
            if i > 1:
                dp[i] += dp[j]
            total_counts[i] = dp[i]
            dp[i] %= (10**9 + 7)

    return total_counts[n]

def can_sort(x, n):
    # This function checks if the permutation [x, ..., x-1, n] can be sorted
    for i in range(1, x):
        if i != x - 1 and i < n:
            return False
    return True

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(count_permutations(n))
