from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    memo = {}

    def dp(tail_length, last_node_in_tail):
        if (tail_length, last_node_in_tail) in memo:
            return memo[(tail_length, last_node_in_tail)]

        max_beauty = 0
        for node in range(last_node_in_tail + 1, n):
            new_tail_length = tail_length + 1
            if all(node not in edges for edges in graph.values()):
                continue

            beauty = new_tail_length * (n - node)
            memo[(new_tail_length, node)] = max(dp(new_tail_length, node), beauty)

        return max_beauty

    print(max(dp(0, 0), key=lambda x: x[1]))

if __name__ == "__main__":
    solve()
