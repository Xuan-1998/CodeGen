# Step 1: Read input
n = int(input())  # number of matrices
p = list(map(int, input().split()))  # dimensions of matrices

# Step 2: Initialize a table to store the minimum number of multiplications for each subproblem
dp = [[0] * len(p) for _ in range(len(p))]

# Step 3: Fill up the dp table using bottom-up dynamic programming
for chain_length in range(1, n):
    for i in range(n - chain_length):
        j = i + chain_length
        if chain_length == 1:
            dp[i][j] = 0
        else:
            min_multiplications = float('inf')
            for k in range(i, j):
                left_chain_multiplications = dp[i][k]
                right_chain_multiplications = dp[k + 1][j]
                multiplications = left_chain_multiplications + right_chain_multiplications + p[i] * p[k + 1] * p[j + 1]
                if multiplications < min_multiplications:
                    min_multiplications = multiplications
            dp[i][j] = min_multiplications

# Step 4: Construct the optimal parenthesization of the matrix chain using the dp table
parentheses = []
def construct_parentheses(i, j):
    if i == j:
        return str(ord('A') + i)
    min_split = float('inf')
    for k in range(i, j):
        multiplications = dp[i][k] + dp[k + 1][j]
        if multiplications < min_split:
            min_split = multiplications
            best_k = k
    parentheses.append('(')
    parentheses.append(construct_parentheses(i, best_k))
    parentheses.append(')')
    parentheses.append(construct_parentheses(best_k + 1, j))
    parentheses.append(')')
    return ''.join(parentheses)

print(construct_parentheses(0, n - 1))
