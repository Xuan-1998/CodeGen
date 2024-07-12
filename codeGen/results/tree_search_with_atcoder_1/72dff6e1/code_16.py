python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: there is one way to have an empty sequence
    for j in range(1, N + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if k != j:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= MOD
    
    # Calculate the final answer
    answer = 0
    for j in range(1, N + 1):
        answer += dp[N][j]
        answer %= MOD
    
    print(answer)

if __name__ == "__main__":
    main()

