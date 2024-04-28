import sys

s = input()

dp = [True]
for i in range(1, len(s)):
    dp.append(False)
    
    for j in range(i):
        if (dp[j] and ((i-j) >= 2 and s[j:j+2] == "AB" and s[i-1:i+1] == "BA")):
            dp[i] = True
            break

print("YES" if dp[-1] else "NO")
