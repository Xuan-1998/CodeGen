def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [1] + [0] * (k-1)
        for i in range(1, k+1):
            dp[i] = ((dp[i-1] * (2**(k-i) - 1)) % (10**9+7))
        print(dp[k])

if __name__ == "__main__":
    solve()
