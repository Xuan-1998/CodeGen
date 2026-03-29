from collections import deque

def dfs(node, parent):
    if not memoized[node]:
        memoized[node] = [0]
        for child in children[node]:
            memoized[node].append(dfs(child, node)[0])
        memoized[node][1] = min(memoized[node])

def main():
    global memoized
    T = int(input())
    for _ in range(T):
        n = int(input())
        parents = list(map(int, input().split()))
        ranges = [list(map(int, input().split())) for _ in range(n)]
        children = [[] for _ in range(n + 1)]
        memoized = {i: None for i in range(1, n + 1)}
        for i in range(2, n + 1):
            children[parents[i - 1]].append(i)
        result = 0
        queue = deque([(1, -float('inf'))])  # (node, min_value)
        while queue:
            node, min_value = queue.popleft()
            for i in range(len(memoized[node])):
                memoized[node][i] += min_value
            if memoized[node]:
                result += memoized[node][1]
                for child in children[node]:
                    queue.append((child, memoized[node][0]))
        print(result)

if __name__ == "__main__":
    main()
