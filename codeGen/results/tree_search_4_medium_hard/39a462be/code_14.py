import sys

def solve():
    A = input().strip()
    B = input().strip()

    n = len(A)
    m = len(B)

    dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(n+1)]

    max_similarities = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j][1] = dp[i-1][j-1][1] + 1
                max_similarities = max(max_similarities, 
                                         4*dp[i][j][1] - (i+j))
            else:
                dp[i][j][1] = max(dp[i-1][j][1], 
                                   dp[i][j-1][1])
            for k in range(2, min(i, j)+1):
                if A[i-k] == B[j-k]:
                    dp[i][j][k] = dp[i-k][j-k][k] + 1
                    max_similarities = max(max_similarities, 
                                             4*dp[i][j][k] - (i+j))
                else:
                    dp[i][j][k] = max(dp[i-k][j][k], 
                                       dp[i][j-k][k])

    print(max_similarities)

if __name__ == "__main__":
    solve()
