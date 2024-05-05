from collections import defaultdict

def solve(t, substrings):
    memo = defaultdict(int)
    def dp(state, pos):
        if state == len(t): return 0
        if (state, pos) in memo: return memo[(state, pos)]
        steps = float('inf')
        for s_i in substrings:
            if t[pos:].startswith(s_i):
                new_state = state + len(s_i)
                new_pos = pos + len(s_i)
                steps = min(steps, dp(new_state, new_pos) + 1)
        memo[(state, pos)] = steps
        return steps

    return dp(0, 0)

t = input().strip()
n = int(input())
substrings = [input().strip() for _ in range(n)]

result = solve(t, substrings)
if result == -1: print(-1)
else:
    m = result
    for j in range(m):
        w_j, p_j = ...  # implement the logic to output the pair of indices
        print(f"{w_j} {p_j}")
