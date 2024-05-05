import sys

def longest_increasing_subsequences_count(arr):
    n = len(arr)
    dp = [1] * n
    memo = {}

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

        memo[i] = dp[i]

    return sum(1 for x in memo.values() if x == max(memo.values()))

# Read the array from standard input
n = int(input())
arr = list(map(int, input().split()))
print(longest_increasing_subsequences_count(arr))
