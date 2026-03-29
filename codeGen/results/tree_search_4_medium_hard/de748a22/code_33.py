def solve(n, q):
    pos_count = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i] == '+':
            pos_count[i] = pos_count[i - 1] + 1
        else:
            pos_count[i] = pos_count[i - 1] - 1

    dp = [float('inf')] * (n // 2 + 1)
    dp[0] = 0

    for l, r in queries:
        while l > 0 and pos_count[l - 1] == 0:
            l -= 1
        while r < n and pos_count[r] == 0:
            r += 1
        new_positives = pos_count[r] - pos_count[l]
        for j in range(max(0, l - 1), min(n, r)):
            dp[j] = min(dp[j], dp[max(0, j - 1)] + new_positives)
    return [dp[i] for i in range(q)]

n, q = map(int, input().split())
a = input()
queries = []
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

print(*solve(n, q), sep='\n')
