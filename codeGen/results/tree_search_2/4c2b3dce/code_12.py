s = input()

dp = [False] * (len(s) + 1)
dp[0] = True

for i in range(3, len(s) + 1):
    if s[i-2:i] == 'BA' and s[i-5:i-2] == 'AB':
        dp[i] = dp[i-3]
    else:
        dp[i] = dp[i-1]

print("YES" if dp[-1] else "NO")
