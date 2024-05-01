from collections import defaultdict

str1 = input()
str2 = input()

dp = defaultdict(int)
for i in range(len(str1)):
    for j in range(i+1):
        c = str1[j:i+1]
        if c in str2:
            dp[c] = max(dp.get(c, 0), dp.get(str1[j-1:i], 0) + 1)
        else:
            dp[c] = dp.get(c, 0)

print(max(dp.values()))
