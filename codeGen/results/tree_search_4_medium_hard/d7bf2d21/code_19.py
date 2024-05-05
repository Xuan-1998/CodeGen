def longest_increasing_subsequences(arr):
    n = len(arr)
    max_val = max(arr)

    dp = [[-1] * (max_val + 1) for _ in range(n)]
    memo = {i: None for i in range(n)}

    for i in range(n):
        for j in range(i, n):
            val = arr[j]
            if dp[i][val] == -1:
                dp[i][val] = 1
            else:
                dp[i][val] = max(dp[i][val], dp[i-1][arr[i-1]] + 1) if i > 0 and arr[i-1] < val else 1

    for i in range(n):
        memo[i] = dp[i][dp[i].index(max(dp[i]))]

    count = 0
    for i in range(n):
        if memo[i] >= 1:
            count += 1

    return count

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(longest_increasing_subsequences(arr))
