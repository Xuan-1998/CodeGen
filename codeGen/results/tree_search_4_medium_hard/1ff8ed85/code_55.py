import sys

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    dp = [True]
    for i in range(1, n):
        if not dp[i-1]:
            break
        if (b[i-1] % 2) != len(str(b[i-1]).replace('0', '')) % 2:
            dp.append(False)
        else:
            dp.append(True)

    print('YES' if dp[-1] else 'NO')
