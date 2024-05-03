def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[False for _ in range(sum(arr) + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, sum(arr) + 1):
            if arr[i - 1] == j:
                dp[i][j] = True
            elif j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = False

    return "YES" if any(dp[n][i] for i in range(sum(arr) + 1)) else "NO"

for _ in range(int(input())):  # Read the number of test cases
    print(can_make_zero())
