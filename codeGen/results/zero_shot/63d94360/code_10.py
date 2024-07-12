python
MOD = 1000000007

def solve(N, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Start with player 0
    
    for i in range(1, N + 1):
        for j in range(K + 1):
            dp[i][j] = 0
            for m in range(K + 1):
                if m != j:
                    dp[i][j] = (dp[i][j] + dp[i - 1][m]) % MOD
    
    return dp[N][0]  # We want the ball to be with player 0 after N passes

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
        results.append(solve(N, K))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

