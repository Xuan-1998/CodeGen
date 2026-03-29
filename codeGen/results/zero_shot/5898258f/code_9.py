def solve():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        dp = [0] * (N + 1)
        for i in range(2, N + 1):
            dp[i] = max(dp[j] + sum(a ^ b for a, b in zip(A[:i], A[1:i])), j=2 to i)
        print(max(dp))

if __name__ == "__main__":
    solve()
