code
import sys

n, k = map(int, input().split())
s = input()

dp = {(0, 'start'): (s[0], 'start')}

for i in range(n-1):
    dp[(i+1, 'delete')] = dp[(i, 'delete')]
    
for i in range(k):
    dp[(i, 'duplicate')] = (s[:i] + s[i:], 'duplicate')

for prefix_length in range(k+1):
    for operation in ['delete', 'duplicate']:
        if operation == 'delete' and prefix_length < n:
            dp[(prefix_length, 'delete')] = min(dp[(i, 'delete')][0] + (s[prefix_length], 'delete') for i in range(prefix_length+1))
        elif operation == 'duplicate':
            if prefix_length > 0:
                dp[(prefix_length, 'duplicate')] = min((dp[i, 'duplicate'][0] + s[0] for i in range(min(prefix_length, k))), default=dp[(0, 'start')])[0]
            else:
                dp[(prefix_length, 'duplicate')] = (s[:k], 'duplicate')

answer = sorted(list(dp.values()))[0][0]

print(answer)
