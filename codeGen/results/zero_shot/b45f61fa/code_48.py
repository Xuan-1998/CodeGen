# Step 1: Read input
n = int(input())
p = list(map(int, input().split()))

# Step 2: Create a table to store the minimum number of multiplications for each subproblem
dp = [[0] * len(p) for _ in range(len(p))]

# Step 3: Fill the table using dynamic programming
for i in range(n-1):
    dp[i][i+1] = (p[i] * p[i+1]) * (p[i] * p[i+1])

for length in range(2, n):
    for start in range(n - length):
        end = start + length
        min_val = float('inf')
        for k in range(start, end):
            left_cost = dp[start][k]
            right_cost = dp[k+1][end]
            min_val = min(min_val, left_cost + right_cost)
        dp[start][end] = min_val

# Step 4: Print the optimal parenthesization
def get_parentheses(start, end):
    if start == end:
        return str(ord('A') + start - 1)
    min_val = float('inf')
    for k in range(start, end):
        left_cost = dp[start][k]
        right_cost = dp[k+1][end]
        if left_cost + right_cost < min_val:
            min_val = left_cost + right_cost
            best_k = k
    return f"({get_parentheses(start, best_k)}{get_parentheses(best_k+1, end)})"

print(get_parentheses(0, n-1))
