from collections import defaultdict

def min_steps_to_color_all_red(t, s):
    memo = {(0, 0): 0}
    for i in range(1, len(t) + 1):
        for j in range(n+1):
            if (i-1, j) in memo:
                memo[(i, j)] = min(memo.get((i-1, j), float('inf')), 
                                    max(memo.get((i-1, j), -1), 
                                        0 if not any(s[k] in t[i:] for k in range(j+1)) else
                                        1 + memo[(i-1, j-1)].get(min(k for s_k in s[:j+1] if s_k in t[i:]), -1)))
            else:
                memo[(i, j)] = float('inf')
    return memo.get((len(t), n), -1)

t = input().strip()
n = int(input())
s = [input().strip() for _ in range(n)]
print(min_steps_to_color_all_red(t, s))
