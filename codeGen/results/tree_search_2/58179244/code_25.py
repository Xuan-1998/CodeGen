import sys

def min_recolors():
    n = int(input())
    colors = input().strip()

    dp = {}
    for i, c in enumerate(colors):
        if i == 0:
            # base case: first lamp needs to be recolored
            dp[(i, c)] = 1
        else:
            last_color = colors[i-1]
            if c == last_color:
                # need to recolor this lamp
                dp[(i, c)] = dp.get((i-1, last_color), float('inf')) + 1
            else:
                # no need to recolor this lamp (already diverse)
                dp[(i, c)] = dp.get((i-1, last_color), 0)

    min_recolors = float('inf')
    for i in range(n):
        if i == 0:
            continue
        c = colors[i]
        last_c = colors[i-1]
        recolors = dp[(i, c)]
        if recolors < min_recolors:
            min_recolors = recolors

    print(min_recolors)

if __name__ == "__main__":
    min_recolors()
