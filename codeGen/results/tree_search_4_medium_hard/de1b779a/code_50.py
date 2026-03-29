from collections import defaultdict

n, m, c0, d0 = map(int, input().split())
memo = {(c0, tuple()): 0}

dp = {}
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    
    for dough_left in range(n+1):
        if dough_left >= c0:
            dp[(dough_left, (ai, bi, ci))] = max(dp.get((dough_left-ci, (ai, bi, ci)), 0) + di - (bi + ci), d0)
        
        for stuff in [(ai, bi, ci)]:
            if dough_left >= c0 and dp.get((dough_left-ci, stuff), -float('inf')) > 0:
                dp[(dough_left, stuff)] = max(dp.get((dough_left-ci, stuff), 0) + di - (bi + ci), d0)

print(max(dp.values()))
