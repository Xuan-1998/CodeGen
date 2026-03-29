from collections import defaultdict

def solve():
    t = int(input())
    MOD = 10**9 + 7
    for _ in range(t):
        n, k = map(int, input().split())
        dp = defaultdict(int)
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(k-1, -1, -1):
                if not (j & (k-1)): # all elements in the range [i-m, i) have a bitwise AND with j
                    dp[i][j] = sum(dp[m][j-1] for m in range(i)) % MOD
                else:
                    dp[i][j] = 0
        print(sum(1 for x in dp.values()) % MOD)

if __name__ == "__main__":
    solve()
