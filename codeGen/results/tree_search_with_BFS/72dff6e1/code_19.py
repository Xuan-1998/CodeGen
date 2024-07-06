MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # dp[i][j] represents the number of valid sequences of length i ending with element j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Initialize base cases: dp[0][0] = 1 (an empty sequence is valid)
    dp[0][0] = 1
    
    # Occurrence count for each element in the sequence
    count = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == 1:
                if A[j - 1] >= 1:
                    dp[i][j] = 1
            else:
                for k in range(1, N + 1):
                    if k != j and count[i - 1][k] < A[k - 1]:
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
            count[i][j] = count[i - 1][j] + (1 if dp[i][j] > 0 else 0)
    
    # Compute the result
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)

if __name__ == "__main__":
    main()

