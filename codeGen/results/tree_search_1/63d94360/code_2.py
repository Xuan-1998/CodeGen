MOD = 1000000007

def calculate_ways(N, K):
    dp = [0] * (N + 1)
    dp[0] = 1  # Messi starts with the ball

    for i in range(1, N + 1):
        dp[i] = (dp[i - 1] * (K - 1)) % MOD

    return dp[N]

def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        print(calculate_ways(N, K))

if __name__ == "__main__":
    main()
