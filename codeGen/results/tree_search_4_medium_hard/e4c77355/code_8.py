code
def longest_increasing_subsequence():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [-1] * (n + 1)

    for i in range(n):
        if dp[i] == -1:
            dp[i] = 1
        else:
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(longest_increasing_subsequence())
