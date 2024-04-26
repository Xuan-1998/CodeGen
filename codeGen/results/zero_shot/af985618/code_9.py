MOD = 998244353

def add_mod(a, b, mod):
    return (a + b) % mod

def solve(n, operations):
    # Initialize the dynamic programming table
    # dp[i][j] will store the sum of all f(B) for subsequences with i '+' operations and j '-' operations
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    plus_count = 0
    minus_count = 0
    for op in operations:
        if op[0] == '+':
            plus_count += 1
            x = op[1]
            # Update the DP table for the '+' operation
            for i in range(plus_count - 1, -1, -1):
                for j in range(minus_count + 1):
                    dp[i + 1][j] = add_mod(dp[i + 1][j], dp[i][j] * x, MOD)
        else:
            minus_count += 1
            # Update the DP table for the '-' operation
            for i in range(plus_count + 1):
                for j in range(minus_count - 1, -1, -1):
                    dp[i][j + 1] = add_mod(dp[i][j + 1], dp[i][j], MOD)

    # Calculate the final answer
    answer = 0
    for i in range(1, n + 1):
        answer = add_mod(answer, dp[i][minus_count], MOD)
    return answer

# Read input from stdin
n = int(input())
operations = []
for _ in range(n):
    line = input().split()
    if line[0] == '+':
        operations.append(('+', int(line[1])))
    else:
        operations.append(('-',))

# Solve the problem and print the answer
print(solve(n, operations))
