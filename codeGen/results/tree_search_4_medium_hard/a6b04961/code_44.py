import sys

n, m = map(int, input().split())
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

def dfs(tail_len, spines):
    if dp[tail_len][spines] != -1:
        return dp[tail_len][spines]

    max_beauty = 0
    for i in range(m):
        u, v = map(int, input().split())
        if u not in tail or v not in tail: # only consider edges that don't have both endpoints in the tail
            new_spines = spines + (1 if (u not in tail and v in tail) or (v not in tail and u in tail) else 0)
            beauty = (tail_len+1) * new_spines
            for j in range(tail_len, -1, -1):
                max_beauty = max(max_beauty, dfs(j, new_spines))

    dp[tail_len][spines] = max_beauty
    return max_beauty

max_tail_len = 0
for i in range(n+1):
    if i == 0:
        continue
    for j in range(i):
        max_tail_len = max(max_tail_len, dfs(j, 0))
print(max_tail_len)
