from collections import defaultdict

n = int(input())
str1 = input()
str2 = input()

dp = defaultdict(int)
for i in range(n):
    for j in range(i+1, n):
        substr = str1[i:j+1]
        dp[substr] += 1
max_common = 0
seen = set()
for i in range(n):
    for j in range(i+1, n):
        substr = str2[i:j+1]
        if substr in seen:
            continue
        seen.add(substr)
        max_common = max(max_common, min(dp[substr], dp.get(substr[:len(substr)//2]), 0))
print(max_common)
