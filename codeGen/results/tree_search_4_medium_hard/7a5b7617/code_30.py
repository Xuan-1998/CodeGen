import sys

def solve():
    T = int(sys.stdin.readline())
    MOD = 1000000000

    dp = [[0] * (2001) for _ in range(2001)]

    for i in range(T):
        N, M = map(int, sys.stdin.readline().split())
        ans = 0
        for s in range(M+1):
            ans += (dp[N-1][s] if s <= M else 0)
        print(ans % MOD)

if __name__ == "__main__":
    solve()
