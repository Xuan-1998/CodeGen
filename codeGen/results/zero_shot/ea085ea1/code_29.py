n = int(input())
str1 = input()
str2 = input()

dp1, dp2 = [[0] * (n + 1) for _ in range(n + 1)], [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp1[i][j] = dp1[i - 1][j - 1] + 1
            dp2[i][j] = max(dp2[i - 1][j], dp2[i][j - 1])
        else:
            dp1[i][j] = max(dp1[i - 1][j], dp1[i][j - 1])
            dp2[i][j] = min(dp2[i - 1][j], dp2[i][j - 1])

ans = []
i, j = n, n
while i > 0 and j > 0:
    if str1[i - 1] == str2[j - 1]:
        ans.append(str1[i - dp2[i][j]:i])
        i -= dp2[i][j]
        j -= dp2[i][j]
    elif dp1[i - 1][j] > dp1[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(len(ans))
