from collections import defaultdict
n = int(input())
str1 = input()
str2 = input()

dp1 = defaultdict(int)
dp2 = defaultdict(int)

for i in range(n):
    for j in range(i+1, n):
        substr1 = str1[i:j]
        dp1[substr1] += 1

for i in range(n):
    for j in range(i+1, n):
        substr2 = str2[i:j]
        dp2[substr2] += 1

count = 0
seen = set()

for key, val in dp1.items():
    if key in dp2:
        count += min(val, dp2[key])
        seen.add(key)

print(count)
