from collections import defaultdict

def distinct_sum_sets(nums):
    dp = defaultdict(set)
    dp[(), 0].add(0)

    for num in nums:
        for s, total in list(dp.items()):
            dp[s | {num}, total + num].update(j + num for j in dp[s, total] if j + num not in dp[s | {num}, :])
            dp[s | {num}, total - num].add(j - num for j in dp[s, total] if j - num not in dp[s | {num}, :])

    return sorted({sum(s) for s in dp})

# Read input from stdin
N = int(input())
nums = [int(x) for x in input().split()]

print(*distinct_sum_sets(nums), sep=' ')
