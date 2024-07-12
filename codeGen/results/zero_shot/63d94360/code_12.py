python
MOD = 1000000007

def count_ways(N, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Assuming the ball starts with player 0

    for i in range(1, N + 1):
        for j in range(K + 1):
            dp[i][j] = sum(dp[i-1][x] for x in range(K + 1) if x != j) % MOD

    return dp[N][0]  # We want the number of ways to pass the ball N times such that it ends with player P (player 0)

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
        results.append(count_ways(N, K))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

