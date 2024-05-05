import sys

def dfs(node, parent, memo):
    if node == -1:  # base case: empty tree
        return True
    xor_value = memo[node] = values[node]
    for child in children[node]:
        if child != parent:
            xor_value ^= memo[child]
            if xor_value != memo[child]:
                return False
    return True

def solve(k):
    states = [False] * n
    for i in range(n):
        states[i] = dfs(i, -1, [0] * n)
    for state in states:
        if state:
            return "YES"
    return "NO"

# input processing omitted for brevity

k, n = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))
children = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    children[u].append(v)
    children[v].append(u)

print(solve(k))
