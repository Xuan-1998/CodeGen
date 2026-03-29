import sys

def solve():
    n = int(input())
    M = list(map(int, input().split()))
    dp = [[0] * (n+1) for _ in range(n+1)]
    k = 0

    for i in range(1, n+1):
        for j in range(i):
            if M[j-1] < i:
                continue
            for last_bit in range(k+1):
                dp[i][last_bit] += (dp[j][last_bit] + dp[i-j-1][last_bit ^ 1]) % (10**9 + 7)
        k = max(k, i)

    print(sum(dp[n]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
