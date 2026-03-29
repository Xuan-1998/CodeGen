def solve(N, M, C, U, L):
    dp = [0] * (C + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(C, U[i - 1] - 1, -1):
            dp[j] += dp[j - 1]

    dp = [0] * (C + 1)
    dp[0] = 1

    for i in range(1, M + 1):
        for j in range(C, L[i - 1] - 1, -1):
            dp[j] += dp[j - 1]

    return [pow(10, 9) + 7 - (dp[i] % (pow(10, 9) + 7)) for i in range(C + 1)]

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        print(*solve(N, M, C, U, L))
