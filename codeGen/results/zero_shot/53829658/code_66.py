import sys

def solve():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
    
    # Find the root of the tree
    root = None
    for i in range(1, n+1):
        if not any(j in graph[i] for j in range(n+1)):
            root = i
            break
    
    # Calculate the number of roads that need to be reversed for each possible capital city
    min_reversals = float('inf')
    capitals = []
    for i in range(1, n+1):
        if i != root:
            reversals = 0
            for j in graph[i]:
                if j != root:
                    reversals += 1
            if reversals < min_reversals:
                min_reversals = reversals
                capitals = [i]
            elif reversals == min_reversals:
                capitals.append(i)
    
    # Output the minimum number of roads that need to be reversed and all possible ways to choose the capital
    print(min_reversals)
    for i in sorted(capitals):
        print(i, end=' ')
    print()

if __name__ == '__main__':
    solve()
