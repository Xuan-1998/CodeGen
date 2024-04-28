s = input()
n = len(s)
dp = [[False for _ in range(n)] for _ in range(n)]
max_length = 0
ans = ""

for i in range(n):
    dp[i][i] = True
    ans = s[i]
    max_length = 1

for i in range(n-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = True
        max_length += 2
        ans = s[i:i+max_length]

for length in range(3, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        if s[i] == s[j]:
            if dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_length:
                    max_length = length
                    ans = s[i:j+1]

print(ans)
