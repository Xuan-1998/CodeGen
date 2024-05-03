from collections import defaultdict

def make_array_zero(dp):
    n, k = len(a), sum(1 for x in a if x > 0)
    memo = defaultdict(lambda: [False] * (k + 1))
    
    for i in range(n):
        for j in range(min(i+1, k+1)):
            if i == 0:
                memo[i][j] = all(x <= 0 for x in a)
            elif a[i-1] > 0 and j > 0:
                memo[i][j] = memo[i-1][j-1] and a[i-1] <= k or memo[i-1][j]
            elif a[i-1] < 0 and j > 0:
                memo[i][j] = memo[i-1][j-1] and a[i-1] >= -k or memo[i-1][j]
            else:
                memo[i][j] = memo[i-1][j]
    
    return "YES" if memo[n-1][k] else "NO"


while True:
    n = int(input())
    if n == 0: break
    a = [int(x) for x in input().split()]
    print(make_array_zero(a))
