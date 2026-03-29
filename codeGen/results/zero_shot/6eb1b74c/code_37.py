def min_steps(i, colored):
    if i == len(text):
        return 0 if colored else -1
    dp[i] = float('inf')
    for s in strings:
        if text[i:i+len(s)] == s:
            dp[i] = min(dp[i], min_steps(i + len(s), True) + 1)
    return dp[i]

text = input()
n = int(input())
strings = [input() for _ in range(n)]
dp = {i: float('inf') for i in range(len(text))}

min_steps_needed = min_steps(0, False)

if min_steps_needed == -1:
    print(-1)
else:
    for j in range(min_steps_needed):
        w_j, p_j = ...  # implement this step
        print(f"{w_j} {p_j}")
