MOD = 998244353

def solve(N, A):
    # Initialize dp table with dimensions (N+1) x (N+1)
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Base case: sequences of length 1
    for j in range(1, N+1):
        dp[1][j] = 1
    
    # Count occurrences of each element in the sequences
    count = [[0] * (N+1) for _ in range(N+1)]
    
    for length in range(2, N+1):
        for last in range(1, N+1):
            for prev in range(1, N+1):
                if count[length-1][prev] < A[prev-1] and count[length-1][last] < A[last-1]:
                    dp[length][last] = (dp[length][last] + dp[length-1][prev]) % MOD
            count[length][last] = sum(dp[length][last] for last in range(1, N+1))
    
    # Sum up all valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N+1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    print(solve(N, A))

