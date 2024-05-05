import math

dp = {0: 1}
min_length = n
max_length = 0
total_ways = 0

for i in range(1, n+1):
    dp[i] = {}
    for j in range(i):
        if all(ord(c) - 97 <= a[ord(c) - 97] for c in s[j:i]):
            if i not in dp:
                dp[i][j] = (dp.get(j, 0) or 0) * a[ord(s[j].lower()) - 97]
            else:
                dp[i][j] = (dp[j] or 0) * a[ord(s[j].lower()) - 97]

    if dp[i]:
        total_ways += sum(dp[k].get(j, 0) or 0 for k in range(j+1, i)) % (10**9 + 7)
        min_length = min(min(k - j for k, v in dp[i].items() for j in range(len(v))), min_length)
        max_length = max(max(k - j for k, v in dp[i].items() for j in range(len(v))), max_length)

print(total_ways % (10**9 + 7))
print(max_length)
print(min_length)
