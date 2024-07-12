python
MOD = 1000000007

def ball_passing_ways(N, K):
    # Initialize the dp table
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # Base case: Initially, the ball is with player 0
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(K + 1):
            dp[i][j] = sum(dp[i-1][m] for m in range(K + 1) if m != j) % MOD
    
    # We want the number of ways to pass the ball exactly N times so that player 0 receives it last
    return dp[N][0]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        result = ball_passing_ways(N, K)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

