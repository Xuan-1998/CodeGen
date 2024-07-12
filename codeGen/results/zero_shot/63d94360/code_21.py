python
MOD = 1000000007

def solve(N, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Start with player 0 with 0 passes

    for i in range(1, N + 1):
        for j in range(K + 1):
            dp[i][j] = sum(dp[i-1][l] for l in range(K + 1) if l != j) % MOD

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
        results.append(solve(N, K))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

