code = """
n, prev_val = 1, None
dp = [False] * (10**5 + 1)
max_len = n - 1

for segment in b:
    if segment > prev_val + 1:
        dp[prev_val] = True
        max_len = prev_val
    elif segment == prev_val:
        i = segment
        while i <= max_len and not dp[i]:
            i += 1
        if i <= max_len:
            dp[segment] = True

for i in range(n):
    if dp[i-1] and abs(b[i]-b[i-1]) == 1:
        print('YES')
        break
else:
    print('NO' if dp[n-1] else 'NO')
"""

print(code)
