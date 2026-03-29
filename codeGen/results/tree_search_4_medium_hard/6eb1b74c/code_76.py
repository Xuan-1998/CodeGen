t = input().strip()
n = int(input())
s = [input().strip() for _ in range(n)]
m = color_red(t, s)
if m == float('inf'):
    print(-1)
else:
    steps = 0
    used = set()
    pos = 0
    while pos < len(t):
        min_steps = float('inf')
        for i, s_i in enumerate(s):
            if s_i not in t[pos:]:
                continue
            new_used = used | {s_i}
            if dp(pos, new_used) + 1 < min_steps:
                steps += 1
                pos += len(s[i])
                used = new_used
    print(m)
    for i in range(steps):
        print(f"{i+1} {pos}")
