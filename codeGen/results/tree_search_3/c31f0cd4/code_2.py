import itertools

def distinct_sum_sums(arr):
    arr.sort()
    max_sum = sum(arr)
    dp = [[0] * (max_sum + 1) for _ in range(len(arr) + 1)]

    for i in range(1, len(arr) + 1):
        for j in range(1, max_sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + (1 if j - arr[i - 1] >= 0 else 0)
                for k in range(i - 1, -1, -1):
                    if j - arr[k] >= 0 and dp[k][j - arr[k]] > 0:
                        dp[i][j] += 1
            else:
                dp[i][j] = dp[i - 1][j]

    return ' '.join(str(sum) for sum in set([sum for i in range(len(arr) + 1) for j in range(max_sum + 1) if dp[i][j]]))

# Read input from stdin
N = int(input())
arr = list(map(int, input().split()))

print(distinct_sum_sums(arr))
