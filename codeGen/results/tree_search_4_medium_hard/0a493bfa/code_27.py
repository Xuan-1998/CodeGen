import sys

def solve():
    n, m = map(int, input().split())
    bad_primes = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(m+1):
            if i == 1:
                dp[i][j] = arr[0]
            elif j == 0:
                dp[i][j] = sum(arr[:i])
            else:
                dp[i][j] = max(dp[i-1][k-1] for k in range(1, min(i+1, m+2))) + i - 1
                if arr[0] not in bad_primes:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1])

    print(max(dp[n]))

if __name__ == "__main__":
    solve()
