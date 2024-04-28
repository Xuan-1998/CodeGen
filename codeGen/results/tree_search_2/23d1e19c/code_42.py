from collections import defaultdict

def process_input():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    return n, m, graph, k, path

def main():
    n, m, graph, k, path = process_input()

    memo = {}
    for i in range(1, n+1):
        for j in range(k+1):
            memo[(i, j)] = float('inf')

    for i in range(n):
        for j in range(i+1, n+1):
            if (i, j) in memo:
                continue
            shortest_dist = float('inf')
            for prev_i in range(i-1, -1, -1):
                if (prev_i, j) not in memo or memo[(prev_i, j)] == 0:
                    break
                shortest_dist = min(shortest_dist, memo[(prev_i, j)] + 1)
            memo[(i, j)] = shortest_dist

    min_recomps = float('inf')
    max_recomps = 0
    for i in range(1, n+1):
        prev_i = i-1 if i > 1 else k-1
        min_recomps = min(min_recomps, memo[(prev_i, 0)] + 1)
        max_recomps = max(max_recomps, memo[(i, k)])

    print(min_recomps, max_recomps)

if __name__ == '__main__':
    main()
