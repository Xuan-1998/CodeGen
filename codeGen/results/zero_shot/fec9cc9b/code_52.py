import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
queries = []
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    queries.append((l, r))

def is_ladder(sub):
    increasing = True
    decreasing = False
    for i in range(1, len(sub)):
        if sub[i] > sub[i-1]:
            decreasing = True
        elif sub[i] < sub[i-1] and not decreasing:
            return "No"
    return "Yes" if not increasing else "No"

for l, r in queries:
    sub = arr[l-1:r]
    print(is_ladder(sub))
