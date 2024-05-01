from collections import defaultdict

def subsetSums(arr):
    n = len(arr)
    max_sum = sum(arr)
    dp = [[[False] * (max_sum + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, n) + 1):
            for k in range(max_sum + 1):
                if k == 0:
                    dp[i][j][k] = True
                elif k >= arr[i - 1]:
                    dp[i][j][k] = dp[i - 1][j][k - arr[i - 1]] or dp[i - 1][j - 1][k]

    unique_sums = set()
    for i in range(1, n + 1):
        for j in range(1, min(i, n) + 1):
            for k in range(max_sum + 1):
                if dp[i][j][k]:
                    unique_sums.add(k)

    return ' '.join(map(str, sorted(list(unique_sums))))

n = int(input())
arr = list(map(int, input().split()))
print(subsetSums(arr))
