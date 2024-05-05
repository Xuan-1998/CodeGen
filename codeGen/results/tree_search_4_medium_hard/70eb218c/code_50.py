def min_operations(n, x):
    max_digits = len(str(x))
    dp = [[float('inf')] * (10**max_digits + 1) for _ in range(n+1)]

    def recursive_memoization(x, n):
        if len(str(x)) == n:
            return 0
        if dp[n][x] != float('inf'):
            return dp[n][x]
        if x < 10**(n-1):
            return float('inf')
        result = float('inf')
        for k in range(1, max_digits+1):
            new_x = x * 10**k
            if len(str(new_x)) <= n:
                result = min(result, recursive_memoization(x//10, n-k) + k)
        return result

    return recursive_memoization(x, n)

# Example input: 5 12345
n, x = map(int, input().split())
print(min_operations(n, x))
