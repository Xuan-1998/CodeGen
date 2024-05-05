import sys

def merge(a, b):
    result = []
    while a and b:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a or b)
    return result

def can_merge(n, p):
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        if i == 0:
            dp[i][j] = 1
        else:
            for j in range(min(i+1,n)+1):
                if p[i-1] > p[j-1]:
                    dp[i][j] = dp[i-1][min(j+1,n)] and 1
                elif p[i-1] < p[j-1]:
                    dp[i][j] = dp[min(i,j)-1][0] and 1
                else:
                    for k in range(min(j,n)+1):
                        if dp[i-1][k] and dp[min(i-1,j-k)-1][0]:
                            dp[i][j] = 1
                            break

    return "YES" if dp[n][n] else "NO"

# Read input from stdin
n = int(input())
p = list(map(int, input().split()))

print(can_merge(n, p))
