from math import inf

def multiply_matrices(p):
    n = len(p)
    dp = [[inf] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n):
        dp[i][i] = 0
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = inf
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    return ''.join('A' + str(i) for i in range(1, n))

if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))
    print(multiply_matrices(p))
