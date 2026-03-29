from collections import defaultdict

def min_multiplications(p):
    n = len(p)
    dp = [[float('inf')] * n for _ in range(n)]
    memo = defaultdict(int)

    def calculate_dp(i, j):
        if i == j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        min_multiplications = float('inf')
        for k in range(i+1, j):
            multiplications = calculate_dp(i, k) + calculate_dp(k, j) + p[i]*p[k+1]*p[j]
            if multiplications < min_multiplications:
                min_multipulations = multiplications
        memo[(i, j)] = min_multiplications
        return min_multiplications

    dp[0][n-1] = 0
    for i in range(n):
        for j in range(i+1, n):
            dp[i][j] = calculate_dp(i, j)

    result = []
    i, j = 0, n-1
    while i < j:
        min_multiplications = float('inf')
        k = i+1
        while k <= j:
            multiplications = dp[i][k-1] + dp[k][j] + p[i]*p[k]*p[j]
            if multiplications < min_multipulations:
                min_multiplications = multiplications
                best_k = k
            k += 1
        result.append(chr(ord('A')+i))
        i, j = best_k, j-1

    return ''.join(result)

# Example input
n = int(input())
p = list(map(int, input().split()))

print(min_multiplications(p))
