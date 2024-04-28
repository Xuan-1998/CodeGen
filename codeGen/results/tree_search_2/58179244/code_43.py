from collections import defaultdict

def diverse_garland(n, s):
    memo = defaultdict(int)
    dp_state = (0, None)

    for i in range(1, n + 1):
        prev_color = s[i - 1]
        if i == 1 or prev_color != s[i - 2]:
            same_color = False
        else:
            same_color = True

        if (i, same_color) not in memo:
            if same_color:
                dp_state = (i, prev_color)
            else:
                dp_state = (i, None)

            min_rec_colors = float('inf')
            for j in range(i):
                rec_colors = 1 + (j == 0 or s[j] != prev_color) * memo[(j, same_color)]
                if rec_colors < min_rec_colors:
                    min_rec_colors = rec_colors
                    dp_state = (i, s[j])

            memo[(i, same_color)] = min_rec_colors

    return memo[n, s[0]]

n = int(input())
s = input()
print(1 + diverse_garland(n, s))
