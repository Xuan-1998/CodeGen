code
s = input().strip()
dp = [False] * (len(s) + 1)
for i in range(1, len(s) + 1):
    if i > 1 and s[i-2:i] in ['AB', 'BA']:
        dp[i] = True

found = False
for i in range(len(s)):
    if dp[i]:
        remainder = s[i+2:]
        if 'AB' in remainder or 'BA' in remainder:
            print('YES')
            found = True
            break

if not found:
    print('NO')
