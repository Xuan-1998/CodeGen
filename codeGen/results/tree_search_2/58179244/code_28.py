import sys

# Read input
N = int(input())
colors = list(input())

# Initialize dp dictionary
dp = {k: {} for k in range(N+1)}

def min_recolors(n, prev_colors):
    if n == 0 or len(prev_colors) == 1:
        return 0
    last_color = prev_colors[-1]
    key = (n-1, tuple(sorted(set(prev_colors))))
    if key in dp:
        return dp[key]
    if len(set(prev_colors)) == 1:  # All colors are the same
        recolors = 1
    else:
        recolors = 0
    for i in range(len(prev_colors)-2, -1, -1):
        if prev_colors[i] != last_color:
            break
    if len(set(prev_colors[i+1:])) == 1:  # Next colors are the same
        recolors += min_recolors(n-1, tuple(sorted(set([prev_colors[i+1]] * (n-i-2))))))
    else:
        recolors += min_recolors(n-1, prev_colors[:i+1])
    dp[key] = recolors + 1 if last_color != 'R' else 0
    return dp[key]

print(min_recolors(N, colors))
