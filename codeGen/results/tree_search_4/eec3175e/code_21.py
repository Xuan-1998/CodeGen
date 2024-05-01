import sys

def find_subset_sum_divisible(n, m, S):
    dp = [False] * (m + 1)
    dp[0] = True

    for s in S:
        for i in range(m, -1, -1):
            if i >= s and dp[i - s]:
                dp[i] = True
                break

    return dp[m]

n = int(input())
m = int(input())
S = list(map(int, input().split()))
print(find_subset_sum_divisible(n, m, S))
