import re

# Read the input strings
t = input().strip()
n = int(input())
strings = []
for _ in range(n):
    strings.append(input().strip())

string_indices = {}
for s in strings:
    matches = [(m.start(), m.end()) for m in re.finditer(re.escape(s), t)]
    string_indices[s] = matches

n_steps = float('inf')
for s, indices in string_indices.items():
    for i, (start, end) in enumerate(indices):
        dp = [[float('inf')] * (len(t) + 1)]
        for j in range(len(t)):
            if start <= j < end:
                dp[j][j+1] = min(dp[j][j+1], dp[start-1][end-1] + 1)
        n_steps = min(n_steps, dp[-1][-1])

steps = []
for i in range(n_steps):
    min_cost = float('inf')
    best_string = None
    for s, indices in string_indices.items():
        cost = dp[indices[i][0]][indices[i][1]]
        if cost < min_cost:
            min_cost = cost
            best_string = s
    steps.append((best_string, indices[i][0], indices[i][1]))

print(n_steps)
for step in steps:
    print(*step)
