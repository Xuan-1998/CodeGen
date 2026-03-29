def minMul(p, i, j):
    n = len(p)
    dp = [[float('inf')] * (n) for _ in range(n)]

    # Base case: no matrices left or no more matrices to multiply
    dp[i][j] = 0

    for k in range(i, j+1):
        for l in range(k, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + p[i]*p[k+1]*p[l+1] + dp[k+1][j])

    return dp[0][n-1]

def main():
    n = int(input())  # Number of matrices
    p = list(map(int, input().split()))  # Dimensions of the matrices

    print(minMul(p, 0, len(p)-1))

if __name__ == "__main__":
    main()
