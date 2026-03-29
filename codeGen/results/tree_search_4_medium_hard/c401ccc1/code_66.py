def has_path_query(graph, q):
    n = max(max(u, v) for u, v in graph)
    dp = [False] * (1 << 30)

    for v in range(1, 1 << 30):
        if all((u & v) == v for u, _ in graph if (u, v) in graph):
            for i in range(n+1):
                if ((i >> 29) & 1) and (v & i) == i:
                    dp[v ^ i] = True

    return ["YES" if dp[i] else "NO" for _ in range(q)]

def read_input():
    q = int(input())
    graph = []
    for _ in range(q):
        u, v = map(int, input().split())
        graph.append((u, v))
    return graph, q

if __name__ == "__main__":
    graph, q = read_input()
    print(*has_path_query(graph, q), sep='\n')
