MOD = 1000000007

def main():
    N = int(input().strip())
    dp = [[0, 0] for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to form a sequence with zero sets
    
    for i in range(1, N + 1):
        size, *set_elements = map(int, input().split())
        # Number of ways to end with an element not from the current set
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) * (size - 1) % MOD
        # Number of ways to end with an element from the current set
        dp[i][1] = dp[i - 1][0]
    
    # The answer is the sum of ways to end with or without an element from the last set
    answer = (dp[N][0] + dp[N][1]) % MOD
    print(answer)

if __name__ == "__main__":
    main()