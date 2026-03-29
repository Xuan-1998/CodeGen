def max_beauty(arr):
    n = len(arr)
    bad_primes = set(int(x) for x in input().split())
    dp = [[0, False] for _ in range(n + 1)]

    for i in range(1, n + 1):
        p = min((x for x in range(2, arr[i]) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))))
        dp[i][0] = dp[i - 1][1] or (p not in bad_primes)
        dp[i][1] = dp[i - 1][0]

    return max(dp[-1])

code = """
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = set(int(x) for x in input().split())

print(max_beauty(arr))
"""

print(code)
