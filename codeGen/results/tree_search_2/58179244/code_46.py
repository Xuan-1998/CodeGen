from collections import defaultdict

def min_recolors(s):
    n = len(s)
    dp = defaultdict(lambda: defaultdict(dict))

    for i in range(n):
        same_color = s[i] == s[(i-1)%n]
        prev_color = s[(i-1)%n]

        if i == 0:
            dp[1][(same_color, prev_color)][(s[i], None)] = 1
        else:
            for c in ['R', 'G', 'B']:
                if c != prev_color:
                    new_state = (same_color, c)
                    dp[i][new_state].update({c: v+1 for v in dp[i-1][prev_color].values()})

    min_recolors = float('inf')
    diverse_garland = ''
    last_color = None
    for state in sorted(dp[n-1].items()):
        if state[0] and (state[0][0] or last_color):
            continue
        recolors, garland = state[1], ''
        for i, c in enumerate(s):
            if recolors[c]:
                garland += c
                recolors.pop(c)
            else:
                garland += c
        if len(recolors) < min_recolors:
            min_recolors, diverse_garland = len(recolors), garland

    print(min_recolors)
    print(diverse_garland)

# Example usage:
n = int(input())
s = input().strip()
min_recolors(s)
