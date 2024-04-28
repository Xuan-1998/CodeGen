from collections import defaultdict

def solve():
    n = int(input())
    s = input()

    dp = defaultdict(int)
    dp[(1, s[0])] = 0 if s[0] != 'R' else 1
    for i in range(2, n+1):
        last_color = s[i-1]
        prev_colors = set(s[:i-1])
        dp[(i, last_color)] = min((dp[(i-1, c)] + (c == last_color) for c in 'RGB' if c not in prev_colors)) + 1

    r = dp[(n, s[-1])]
    t = s
    for i in range(n-1, -1, -1):
        if dp[(i+1, s[i])] > dp[(i, s[i])]:
            t = t[:i] + 'RGB'[('R', 'G', 'B')[s[i]] + 2]
            break

    print(r)
    print(t)

solve()
