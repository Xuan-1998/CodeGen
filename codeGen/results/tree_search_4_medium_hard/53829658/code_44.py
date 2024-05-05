import sys
from collections import defaultdict

def read_input():
    n = int(sys.stdin.readline().strip())
    tree = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().strip().split())
        tree[u].append(v)
        tree[v].append(u)
    return n, tree

def find_min_inversions(tree, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        for p in range(n + 1):
            if p == 0:
                dp[i][p] = len(tree[i - 1]) + 1
            else:
                min_dist = sys.maxsize
                for j in tree[i - 1]:
                    min_dist = min(min_dist, dp[j][p - 1])
                dp[i][p] = min_dist + (p > 0)
    return min([dp[i][n - 1] for i in range(2, n + 1)])

def find_all_capitals(tree, n):
    res = [1]
    for i in range(2, n + 1):
        if dp[i][0] < dp[i - 1][0]:
            res.append(i)
        else:
            res.append(i - 1)
    return res

n, tree = read_input()
dp = [[0] * (n + 1) for _ in range(n + 1)]
min_inversions = find_min_inversions(tree, n)
print(min_inversions)

res = find_all_capitals(tree, n)
for city in res:
    print(city, end=' ')
