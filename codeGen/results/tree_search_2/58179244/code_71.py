import sys

n = int(input())
s = input()

dp_states = {(i, prev_color, curr_color): None for i in range(n+1) for prev_color in ['R', 'G', 'B'] for curr_color in ['R', 'G', 'B']}
dp = {0: 0}

for i in range(1, n+1):
    for prev_color in ['R', 'G', 'B']:
        for curr_color in ['R', 'G', 'B']:
            if (i-1, prev_color, curr_color) not in dp_states:
                continue
            recolor_count = 0
            if prev_color == curr_color:
                recolor_count = min(recolor_count + 1, int(dp.get((i-1, prev_color, curr_color), float('inf'))))
            else:
                recolor_count = min(recolor_count + 1, dp.get((i-1, prev_color, curr_color), float('inf')))
            dp[(i, prev_color, curr_color)] = recolor_count

min_recolors = float('inf')
for i in range(1, n+1):
    if s[i-1] == s[i]:
        min_recolors = min(min_recolors, dp.get((i, s[i-1], s[i]), float('inf')))

print(min_recolors)
