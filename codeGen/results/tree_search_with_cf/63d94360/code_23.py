python
MOD = 1000000007

def solve(T, test_cases):
    results = []
    
    for N, K in test_cases:
        # Initialize the dp table
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        dp[0][0] = 1  # Base case: 1 way to start with player 0 and 0 passes
        
        for i in range(1, N + 1):
            for j in range(K + 1):
                dp[i][j] = sum(dp[i-1][m] for m in range(K + 1) if m != j) % MOD
        
        # The result is the number of ways to have exactly N passes ending with player K
        result = dp[N][K]
        results.append(result)
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    test_cases = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(T)]
    
    results = solve(T, test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

