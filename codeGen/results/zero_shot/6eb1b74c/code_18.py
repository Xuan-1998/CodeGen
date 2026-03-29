import sys

def min_steps_to_color_all(t, s):
    n = len(s)
    dp = [[0] * (len(t) + 1) for _ in range(n + 1)]
    used_strings = [False] * (n + 1)

    # Initialize the first row of dp
    for i in range(len(t) + 1):
        dp[0][i] = i

    # Fill up the dp table
    for j in range(1, n + 1):
        for i in range(len(t) + 1):
            if used_strings[j - 1]:
                dp[j][i] = dp[j - 1][i]
            else:
                min_steps = float('inf')
                for k in range(i):
                    if s[j - 1] in t[k:i]:
                        min_steps = min(min_steps, dp[j - 1][k])
                dp[j][i] = min_steps + (i - k)

    # Find the minimum number of steps
    min_steps = float('inf')
    for i in range(len(t) + 1):
        if dp[n][i] < min_steps:
            min_steps = dp[n][i]

    if min_steps == len(t):
        return -1

    # Reconstruct the steps
    steps = []
    j = n
    i = len(t)
    while j > 0 or i > 0:
        if used_strings[j - 1]:
            j -= 1
        else:
            for k in range(i):
                if s[j - 1] in t[k:i]:
                    steps.append((j, k))
                    j -= 1
                    i = k

    return min_steps, len(steps), steps

# Read input from stdin
t = input()
n = int(input())
s = []
for _ in range(n):
    s.append(input())

# Calculate and print the result
min_steps, num_steps, steps = min_steps_to_color_all(t, s)
print(min_steps)
for i in range(num_steps):
    print(*steps[i])
