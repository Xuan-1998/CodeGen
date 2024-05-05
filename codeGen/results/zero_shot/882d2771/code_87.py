import sys

def solve():
    t, l, r = map(int, input().split())
    dp = [0] * (r - l + 1)
    dp[0] = 0
    for i in range(1, r - l + 1):
        dp[i] = dp[i-1] + i

    res = sum(t * dp[i] for i in range(l-r+1)) % (10**9 + 7)
    print(res)

if __name__ == "__main__":
    solve()
