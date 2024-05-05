import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        dp = [0] * (N + 1)
        for i in range(2, N + 1):
            dp[i] = max(dp[i-1], dp[i-2] + A[i-1] ^ A[i])
        print(max(dp))

if __name__ == "__main__":
    solve()
