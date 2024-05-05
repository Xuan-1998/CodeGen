# Step 1: Define variables and read input
n = int(input())  # number of matrices
p = list(map(int, input().split()))  # dimensions of matrices

# Step 2: Create a table to store the minimum number of multiplications needed for each subproblem
dp = [[0] * (len(p) + 1) for _ in range(len(p) + 1)]

# Step 3: Fill up the dp table using dynamic programming
for length in range(2, len(p) + 1):
    i = 0
    while i + length <= len(p):
        j = i + length - 1
        min_multiplier = float('inf')
        for k in range(i, j):
            left_multiplier = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
            if left_multiplier < min_multiplier:
                min_multiplier = left_multiplier
        dp[i][j] = min_multiplier
        i += 1

# Step 4: Construct the optimal parenthesization of the matrix chain
optimal_parenthesis = []
i, j = 0, len(p) - 1
while i < j:
    for k in range(i, j):
        if dp[i][k] + dp[k+1][j] == dp[i][j]:
            optimal_parenthesis.append('A' + str(i))
            optimal_parenthesis.append('A' + str(k+1))
            optimal_parenthesis.append('A' + str(j+1))
            i = k+1
            break
        elif dp[i][k] < dp[i][j]:
            optimal_parenthesis.append('(')
            optimal_parenthesis.append('A' + str(i))
            optimal_parenthesis.append('A' + str(k+1))
            optimal_parenthesis.append(')')
            i = k+1
            break

# Step 5: Print the result
print(''.join(optimal_parenthesis))
