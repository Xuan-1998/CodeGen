import sys
from collections import defaultdict

def solve():
    n = int(input())
    adj_list = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    m = int(input())
    prime_factors = list(map(int, input().split()))
    k = 1
    for p in prime_factors:
        k *= p

    memo = {}
    def dfs(node, parent):
        if node not in memo:
            dp_node = (0, 0, k)
            if len(adj_list[node]) == 1:  # leaf node
                dp_node = (0, 0, k)
            else:
                for child in adj_list[node]:
                    if child != parent:
                        dp_child = dfs(child, node)
                        dp_node = ((dp_child[0] + 1), dp_node[1] + dp_child[2], dp_node[2] * dp_child[2])
            memo[node] = dp_node
        return memo[node]

    max_distribution_index = 0
    for i in range(1, n):
        for j in range(i+1, n):
            node_i_state = dfs(i, -1)
            node_j_state = dfs(j, -1)
            if i != j:
                path_sum = (node_i_state[1] + node_j_state[1]) % (10**9 + 7)
                max_distribution_index = max(max_distribution_index, path_sum)
    print(max_distribution_index)

if __name__ == "__main__":
    solve()
