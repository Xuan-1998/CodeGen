def max_path_sum(tree):
    memo = {}
    def dfs(i):
        if i >= len(tree):
            return 0
        if i in memo:
            return memo[i]
        left = right = 0
        if 2*i+1 < len(tree):
            left = dfs(2*i+1)
        if 2*i+2 < len(tree):
            right = dfs(2*i+2)
        memo[i] = tree[i] + max(left, right)
        return memo[i]
    max_sum = float('-inf')
    for i in range(len(tree)):
        max_sum = max(max_sum, dfs(i))
    return max_sum

import sys
n = int(sys.stdin.readline().strip())
tree = list(map(int, sys.stdin.read(n).split()))
print(max_path_sum(tree))
