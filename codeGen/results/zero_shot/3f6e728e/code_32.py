import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        
        dp = [0] * (C + 1)
        for r in set(U) | set(L):
            for i in range(min(C, r), -1, -1):
                if r > U[i-1]:
                    dp[i] += (dp[i-1] + (r - U[i-1])) % (10**9+7)
        
        print(*dp, sep=' ')

if __name__ == "__main__":
    solve()
