import sys

# Read input and initialize variables
n = int(input())
sequence = list(map(int, input().split()))
memo = {}

def dfs(x, y):
    if (x, y) in memo:
        return memo[(x, y)]
    if x == 0:
        return y
    if x > n:
        new_x, new_y = x - sequence[x-1], y + 2 * sequence[x-1]
    else:
        new_x, new_y = x + sequence[x-1], y + sequence[x-1]
    
    result = dfs(new_x, new_y)
    memo[(x, y)] = result
    return result

for i in range(1, n):
    print(dfs(i+1, 0) if i+1 <= n else -1)
