codeblock
n = int(input())
str1 = input().strip()
str2 = input().strip()

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(min(i, n) + 1):
        if str1[i-k:i+1] == str2[i-k:i+1]:
            if k > 0:
                dp[i][k] = max(dp[i][k], dp[i-1][k-1] + 1)
            else:
                dp[i][k] = 1

print(max(dp[-1]))
endcodeblock
