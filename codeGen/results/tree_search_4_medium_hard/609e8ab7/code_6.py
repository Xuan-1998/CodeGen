from collections import defaultdict

def dfs(node, parent, memo):
    if node not in memo:
        children = 0
        for child in range(1, len(ranges) + 1):
            if child != node and child != parent:
                if ranges[child][0] < ranges[node][1]:
                    children += 1
                    dfs(child, node, memo)
        total = sum(memo[i][0] for i in range(len(ranges)) if ranges[i][1] >= ranges[node][1])
        memo[node] = (max(ranges[node][0], min(x for x in memo)), len(ranges) - children)
    return memo[node]

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        p = list(map(int, input().split()))
        ranges = [list(map(int, input().split())) for _ in range(n)]
        memo = defaultdict(lambda: (float('inf'), 0))
        print(dfs(1, -1, memo)[0])

if __name__ == "__main__":
    solve()
