from collections import defaultdict

def max_points(n, a):
    dp = [0] * (n + 1)
    min_val, max_val = min(a), max(a)
    for val in range(min_val, max_val + 1):
        delete_count = sum(1 for x in a if x == val or x == val - 1 or x == val + 1)
        dp[val] = delete_count + (n - val) * (dp[val - 1] if val > min_val else 0)

    return max(dp)

# Read input from standard input
n = int(input())
a = list(map(int, input().split()))

print(max_points(n, a))
