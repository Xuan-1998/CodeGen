from collections import defaultdict

def min_operations(arr):
    n = len(arr)
    memo = defaultdict(int)

    def dfs(i, target):
        if i >= n:
            return 0
        if (i, target) in memo:
            return memo[(i, target)]
        
        if arr[i] == target:
            return dfs(i + 1, target)

        left_ops = right_ops = float('inf')
        if i > 0 and arr[0] == target:
            left_ops = dfs(0, 0)
        else:
            left_ops = dfs(i - 1, 0) + 1

        if i < n - 1 and arr[-1] == target:
            right_ops = dfs(n - 1, 0)
        else:
            right_ops = dfs(i + 1, 0) + 1

        memo[(i, target)] = min(left_ops, right_ops)
        return memo[(i, target)]

    result = float('inf')
    for i in range(n):
        if arr[i] != 0:
            result = min(result, dfs(i, arr[i]))
    
    if result == float('inf'):
        return 'NO'
    else:
        return 'YES'

# Read the input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
