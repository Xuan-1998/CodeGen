import sys

def count_invertible_matrices(N):
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 2
    
    for t in range(2, N + 1):
        count = 0
        for a in range(t):
            b = t - a
            if a >= b:
                count += 1
        dp[t] = count
        
    count_positive_matrices = 0
    for t in range(N, -1, -1):
        if t % 2 == 1:  # Check if the determinant is positive
            count_positive_matrices += dp[t]
            
    return count_positive_matrices

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count_invertible_matrices(N))
