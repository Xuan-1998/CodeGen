MOD = 1000000007

def find_ways(N, K):
    # Initialize dp array
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # Initial state: ball starts with player 0
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(K + 1):
            dp[i][j] = sum(dp[i-1][m] for m in range(K + 1) if m != j) % MOD
    
    # We need the ball to be with player P after N passes
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
        results.append(find_ways(N, K))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

