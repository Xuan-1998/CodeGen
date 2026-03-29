import sys

def dfs(node, k, subtree):
    if not subtree:
        return 1
    xor_value = subtree[0]
    for child in subtree[1:]:
        child_xor_value = dfs(child, k - 1, [value ^ xor_value for value in subtree[1:]])
        if child_xor_value == 0 or (k > 0 and child_xor_value != xor_value):
            return 0
    return 1

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        values = list(map(int, sys.stdin.readline().split()))
        edges = []
        for _ in range(n - 1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
        if dfs(0, k, [(values[i], i) for i in range(n)]):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
