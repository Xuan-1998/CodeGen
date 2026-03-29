import sys

# Read input from stdin
q = int(sys.stdin.readline())

# Initialize memoization dictionary
memo = {}

def dfs(u, k):
    if (u, k) in memo:
        return memo[(u, k)]

    if k == 0 or u & (1 << k):
        return False

    for v in range(30):  # iterate over all possible vertices
        if (u & (1 << v)) == (1 << v):
            if dfs(v, k-1) and (v & (1 << k)):
                return True

    memo[(u, k)] = False
    return False

# Read queries from stdin and process them
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    if dfs(u, 30):
        print("YES")
    else:
        print("NO")
