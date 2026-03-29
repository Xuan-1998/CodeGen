import sys
from collections import defaultdict, deque

def solve():
    n = int(sys.stdin.readline())
    tree = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        tree[u].append(v)

    # Step 1: Calculate the level of each node
    queue = deque([(1, 0)])  # (node, level)
    levels = {1: 0}
    while queue:
        node, level = queue.popleft()
        for neighbor in tree[node]:
            if neighbor not in levels:
                levels[neighbor] = level + 1
                queue.append((neighbor, level + 1))

    # Step 2: Find the minimum number of roads to be inversed and all possible ways to choose the capital
    min_inversions = float('inf')
    capitals = []
    for city in range(2, n+1):
        if levels[city] % 2 == 0:
            inversions = sum(levels[neighbor] for neighbor in tree[city])
            if inversions < min_inversions:
                min_inversions = inversions
                capitals = [city]
            elif inversions == min_inversions:
                capitals.append(city)

    # Print the result
    print(min_inversions)
    print('\n'.join(map(str, capitals)))

if __name__ == '__main__':
    solve()
