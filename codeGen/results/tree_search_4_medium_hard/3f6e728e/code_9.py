import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [0] * (C + 1)
        for i in range(1, C + 1):
            count_upper = sum(1 for j in range(i) if U[j] == i)
            count_lower = sum(1 for j in range(M) if L[j] == i)
            dp[i] = sum(dp[j] * count_upper * count_lower for j in range(min(i, C)))
        print(' '.join(map(str, dp)))

solve()
