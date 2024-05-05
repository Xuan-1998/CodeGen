===BEGIN CODE===
def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = {(1, 0): 0}
    
    for i in range(2, n+2):
        for x in range(i):
            if (i, x) not in dp:
                if x % 2 == 1:
                    dp[(i, x)] = dp.get((p[i-1], x), float('inf')) + 1
                else:
                    dp[(i, x)] = min(dp.get((p[i-1], x-1), float('inf')), dp.get((p[i-1], x+1), float('inf'))) + 1
    
    return dp.get((n+1, 0), -1)

print(solve())
