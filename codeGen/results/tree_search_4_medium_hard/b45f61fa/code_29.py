import sys

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < dp[i][j]:
                    dp[i][j] = q

    s = ""
    i = 0
    j = n-1
    while j > i:
        k = min(range(i, j), key=lambda x: dp[i][x]+dp[x+1][j])
        if p[k] < p[i]:
            s += "(" + chr(65+i) + "*(" + chr(65+k+1) + ")*" + str(p[k+1]) + ")"
            i = k + 1
        else:
            s += chr(65+j) + "*" + str(p[j])
            j -= 1

    if n > 1:
        s = "(" + s + ")"

    return s

p = list(map(int, input().split()))
print(matrix_chain_order(p))
