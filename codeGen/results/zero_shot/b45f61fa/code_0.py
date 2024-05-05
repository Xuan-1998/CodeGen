def min_num_multiplications(p):
    n = len(p)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for k in range(2, n+1):
        for i in range(n-k+1):
            j = i + k - 1
            if i == j:
                dp[i][j] = 0
            else:
                min_mul = float('inf')
                for split_index in range(i, j+1):
                    mul = dp[i][split_index-1] + dp[split_index][j] + p[i-1]*p[split_index]*p[j]
                    if mul < min_mul:
                        min_mul = mul
                dp[i][j] = min_mul

    # Construct the optimal parenthesization
    i, j = 0, n-1
    mul = dp[0][n-1]
    optimal_parentheses = []
    while i < j:
        for split_index in range(i+1, j):
            if dp[i][split_index-1] + dp[split_index][j] == dp[i][j]:
                optimal_parentheses.append((i+1, split_index))
                i, j = split_index, j
                break

    return ''.join(f'({"".join(map(str, range(i+1, j+1)))})' for i, j in reversed(optimal_parentheses))

# Example input
n = int(input())
p = list(map(int, input().split()))

print(min_num_multiplications(p))
