s = input()
dp = [[False] * len(s) for _ in range(len(s))]
ans = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if s[i:j][::-1] == s[i:j]:
            dp[i][j-1] = True
            ans = s[i:j]
