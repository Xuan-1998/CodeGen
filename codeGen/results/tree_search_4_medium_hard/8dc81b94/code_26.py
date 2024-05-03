def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [[False] * (max(arr) + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for k in range(max(arr) + 1):
            if i == 1:
                dp[i][k] = arr[0] == k
            else:
                if (arr[i - 1] - k) % 2 == 0 and dp[i - 1][k - (arr[i - 1] - k) // 2]:
                    dp[i][k] = True
                elif (k - arr[i - 1]) % 2 == 0 and dp[i - 1][k - (k - arr[i - 1]) // 2]:
                    dp[i][k] = True

    print('YES' if dp[n][0] else 'NO')

if __name__ == "__main__":
    can_make_zero()
