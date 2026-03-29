import sys

def solve():
    n = int(sys.stdin.readline().strip())
    parent = list(map(int, sys.stdin.readline().strip().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().strip().split())
        ranges.append((l, r))

    # Initialize the tree
    tree = [0] * (n + 1)
    for i in range(1, n):
        tree[parent[i]] += 1

    # Calculate the minimum operations required to adjust each node's value within its range
    ops = 0
    for l, r in ranges:
        ops += max(0, l - 1) + (r - l + 1) * (tree[1] - tree[r])

    print(ops)

if __name__ == "__main__":
    solve()
