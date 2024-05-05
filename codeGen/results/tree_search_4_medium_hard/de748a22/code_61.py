def solve():
    n, q = map(int, input().split())
    arr = list(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        majority_sign = -1 if sum(arr[:i]) < 0 else 1
        for j in range(i, n + 1):
            if arr[j-1] == str(majority_sign):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j-1] + (arr[j-1] != str(majority_sign)), dp[i-1][j] + (arr[j-1] == str(majority_sign)))

    for _ in range(q):
        l, r = map(int, input().split())
        print(dp[r][r] - dp[l-1][r])

if __name__ == "__main__":
    solve()
