MOD = 998244353

def add_mod(a, b):
    return (a + b) % MOD

def sub_mod(a, b):
    return (a - b + MOD) % MOD

def mul_mod(a, b):
    return (a * b) % MOD

def solve(n, sequence):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: empty subsequence

    for i in range(1, n + 1):
        if sequence[i - 1][0] == '+':
            x = sequence[i - 1][1]
            for j in range(i + 1):
                dp[i][j] = dp[i - 1][j]  # Skip the current element
                if j > 0:
                    dp[i][j] = add_mod(dp[i][j], mul_mod(dp[i - 1][j - 1], x))
        else:
            for j in range(i + 1):
                dp[i][j] = dp[i - 1][j]  # Skip the current element
                if j > 0:
                    dp[i][j] = add_mod(dp[i][j], dp[i - 1][j - 1])
                dp[i][j] = mul_mod(dp[i][j], 2)

    # Calculate the final answer
    answer = 0
    for j in range(1, n + 1):
        answer = add_mod(answer, dp[n][j])

    return answer

# Read input
n = int(input().strip())
sequence = []
for _ in range(n):
    line = input().strip().split()
    if line[0] == '+':
        sequence.append(('+', int(line[1])))
    else:
        sequence.append(('-', 0))

# Solve the problem
print(solve(n, sequence))
