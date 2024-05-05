import sys

def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * (n) for _ in range(n)]
    s = [""] * (n-1)

    # Fill up the dp table
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            min_val = sys.maxsize
            for k in range(i, j):
                q = p[i] * p[k+1] * p[j]
                val = dp[i][k] + dp[k+1][j] + q
                if val < min_val:
                    min_val = val
                    s[j-i] = "(" + s[k-i+1] + ")*" + str(q)
            dp[i][j] = min_val

    # Print the optimal order of parentheses
    print(s[-1])
