import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = {0: 0}
    
    for x in range(1, n+1):
        y = dp.get(x-1, None)
        if y is not None:
            for _ in range(a[x]):
                dp[x] = (dp.get(x-1, 0) + a[x]) % (n+1)
    
    result = []
    for x in range(2, n+1):
        y = dp.get(x, -1)
        if y is not None:
            result.append(str(y))
        else:
            result.append('-1')
    
    print('\n'.join(result))

if __name__ == "__main__":
    solve()
