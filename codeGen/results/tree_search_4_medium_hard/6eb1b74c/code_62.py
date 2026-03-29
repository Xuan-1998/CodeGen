import sys

def solve(t, n, strings):
    memo = {}
    dp_to_prev_states = []
    dp_table = [float('inf')] * (len(t) + 1)

    def dfs(i, red):
        if i >= len(t):
            return 0 if red == len(t) else -1
        if (i, red) in memo:
            return memo[(i, red)]
        min_steps = sys.maxsize
        for j in range(n):
            token_length = len(strings[j])
            if red + token_length <= len(t) and t[i:i+token_length] == strings[j]:
                steps = dfs(i+token_length, red+token_length)
                if steps != -1:
                    min_steps = min(min_steps, 1 + steps)
        dp_table[i] = min_steps
        memo[(i, red)] = min_steps
        return min_steps

    if len(t) > 0 and dfs(0, 0) == -1:
        return -1, []

    min_steps = dfs(0, 0)
    i = 0
    while min_steps > 0:
        for j in range(n):
            token_length = len(strings[j])
            if i+token_length <= len(t) and t[i:i+token_length] == strings[j]:
                if dp_table[i+token_length] - dp_table[i] == 1:
                    dp_to_prev_states.append((j, i))
                    i += token_length
                    break
        min_steps -= 1

    return dp_table[-1], dp_to_prev_states


# Read input from stdin and print the solution to stdout
t = input().strip()
n = int(input())
strings = [input().strip() for _ in range(n)]
min_steps, steps = solve(t, n, strings)
print(min_steps)

for w, p in steps:
    print(f"({w}, {p})")
