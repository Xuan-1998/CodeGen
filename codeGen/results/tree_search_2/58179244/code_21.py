n = int(input())
colors = input()

dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

dp[0][0][0] = dp[0][0][1] = 0  # base case: no recolors needed for an empty garland

for i in range(1, n + 1):
    for j in range(3):  # consider each possible last color
        prev_colors = tuple(colors[i - 2:i])  # get the colors of the previous two lamps
        min_recolors = float('inf')  # initialize the minimum recolors needed

        for k in range(3):  # consider each possible previous color combination
            if (k != j and prev_colors[0] == 'R' and k == 1) or \
               (k != j and prev_colors[0] == 'G' and k == 2):
                continue  # skip this color combination because it's not diverse

            min_recolors = min(min_recolors, dp[i - 1][k][prev_colors.index('R')]) + (j != k)  # update the minimum recolors needed

        dp[i][j][prev_colors] = min_recolors  # store the result in the DP array

r = dp[n][0][colors.count('R')]
t = ''.join(['R' if i < r else colors[i] for i in range(n)])

print(r)
print(t)
