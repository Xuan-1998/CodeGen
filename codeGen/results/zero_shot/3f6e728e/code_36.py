import sys

def solve():
    dp = {i: [0, 0] for i in range(C+1)}
    dp[0][0] = 1
    for _ in range(int(input())):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        for r in range(1, C+1):
            dp[r][0] = (dp[r-1][0] * sum(1 for u in U if u >= r)) % (10**9 + 7)
            dp[r][1] = (dp[r-1][1] * sum(1 for l in L if l <= r)) % (10**9 + 7)
        print(*[dp[i][0]*dp[C-i][1] for i in range(C+1)], sep=' ')

if __name__ == '__main__':
    solve()
