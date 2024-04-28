N = int(input())
str1 = input()
str2 = input()

dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)

max_len = 0
for i in range(1, N + 1):
    for j in range(i):
        if str1[j:i] == str2[j:i]:
            dp1[i] = max(dp1[i], dp1[j - 1] + 1)
            max_len = max(max_len, dp1[i])

print(max_len)
