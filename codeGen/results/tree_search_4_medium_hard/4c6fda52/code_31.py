code
from collections import defaultdict

dp = defaultdict(int)

def solve():
    n, k = map(int, input().split())
    s = list(input())

    for i in range(n):
        for j in range(min(i+1, k), -1, -1):
            if s[i-j+1:i+1] == [c for _ in range(j) for c in ['R', 'G', 'B']][(i-j)%6:(i)%6]:
                dp[(i, j)] = 0
            else:
                min_changes = float('inf')
                for c in ['R', 'G', 'B']:
                    changes = sum(s[m] != c for m in range(i-j+1, i+1))
                    if dp.get((i-j-1, k), float('inf')) + changes < min_changes:
                        min_changes = dp.get((i-j-1, k), float('inf')) + changes
                dp[(i, j)] = min_changes

    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = list(input())
        print(dp.get((n-1, k-1), -1))

solve()
code
