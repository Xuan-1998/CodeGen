import sys

s = input().strip()

dp = [False]
for i in range(len(s)-1):
    dp.append((s[:i+2].count('A') > s[:i+2].count('B')) != (s[i+2:].count('A') < s[i+2:].count('B')))

print("YES" if any(dp) else "NO")
