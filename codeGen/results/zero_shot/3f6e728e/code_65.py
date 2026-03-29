import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        # Sort the radii in descending order
        U.sort(reverse=True)
        L.sort(reverse=True)

        dp = [0] * (C + 1)
        dp[0] = 1

        for i in range(C):
            if U:
                if U[-1] > i + 1:
                    dp[i + 1] += dp[i]
                    dp[i + 1] %= 10**9 + 7
            if L:
                if L[-1] > i + 1:
                    dp[i + 1] += dp[i]
                    dp[i + 1] %= 10**9 + 7

        print(*dp, sep=' ')

if __name__ == "__main__":
    solve()
