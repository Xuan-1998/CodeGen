import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [0] * (n + 1)
    dp[1] = max(b[0], c[0])  # base case: first hare

    for i in range(2, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] if i > 1 else a[i-1])
        dp[i] += (dp[j-1] if j > 0 else b[i-1])

    print(dp[n])  # return the maximum joy for n hares

if __name__ == "__main__":
    solve()
