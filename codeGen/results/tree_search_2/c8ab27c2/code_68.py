dp = [[[-1 for _ in range(501)] for _ in range(501)]]  # Initialize dp table

S, T = input().split(), input().split()  # Read S and T from stdin
n, m = len(S), len(T)

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 or j == 0:  # Base case: If either string is empty
            dp[i][j] = -1
        elif S[i - 1] != T[j - 1]:  # Transition rule: If characters don't match
            for k in range(j + 1):
                dp[i][j] = min(dp[i][k], dp[i][j])
        else:  # Characters match, so just copy the previous result
            dp[i][j] = dp[i - 1][j - 1]

print(min(max(map(lambda x: sum(1 for y in x if len(y) > 0), zip(*dp))), key=lambda x: (x, dp[x[0]][x[1]])))
