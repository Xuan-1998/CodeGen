from collections import defaultdict

N = int(input())
str1 = input().strip()
str2 = input().strip()

dp1, dp2 = [0] * (N + 1), [0] * (N + 1)
for i in range(N):
    for j in range(i+1):
        if str1[i] == str2[j]:
            dp2[i+1] = max(dp2[i+1], dp1[j] + 1)
        dp1[i+1] = max(dp1[i], 1 if str1[i] == str2[0] else dp1[i])
print(max(dp2))
