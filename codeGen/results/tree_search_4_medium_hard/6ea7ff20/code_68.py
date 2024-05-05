import sys

def merge(a, b):
    if not a:  # a is empty
        return b
    if not b:  # b is empty
        return a
    
    if a[0] <= b[0]:  # a_1 <= b_1
        return [a[0]] + merge(a[1:], b)
    else:  # a_1 > b_1
        return [b[0]] + merge(a, b[1:])
    
n = int(input())
p = list(map(int, input().split()))
dp = [[False] * (n+1) for _ in range(n+1)]

for i in range(n):
    dp[i][i] = True  # base case: if both arrays are empty, p is empty too

for i in range(n-1):
    for j in range(i+1, n):
        if p[i] < p[j]:
            for k in range(j):
                if (p[i] > p[k]) or (i == 0 and p[i] >= p[k]):
                    dp[i][j] = True
                    break
        elif p[i] > p[j]:
            for k in range(i+1, j+1):
                if p[i] <= p[k]:
                    dp[i][j] = True
                    break

if dp[0][n-1]:
    print("YES")
else:
    print("NO")
