n = int(input())
s = input()

dp = [0] * (2*n + 1)
same_color = s[0]

for i in range(1, n):
    same_color = same_color == s[i]
    dp[i*2-1] = same_color
    dp[i*2] = min(dp[i*2-1], dp[i*2-2]) + (1 - same_color)

r = dp[-1]

t = list(s)
for i in range(1, n):
    if t[i-1] == t[i]:
        for _ in range(i+1):
            t.pop(0)
            t.append('R' if 'G' in s else 'G' if 'B' in s else 'B')

print(r)
print(''.join(t))
