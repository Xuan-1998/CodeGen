import sys

def count_nodes(i, j, k):
    # Base case: node i has no children
    if k == 1:
        return [node[i] == j].count(True)

    dp = {}
    for child in children[i]:
        if child not in dp:
            dp[child] = {}
        for xor_val in range(2**20):  # assuming max value is 10^9
            if (xor_val ^ node[child]) == j:
                dp[child][xor_val] = count_nodes(child, xor_val, k-1)

    return sum([dp[child].get(xor_val, [0])[0] + (node[i] == j) for child in children[i]])

def solve():
    n, k = map(int, sys.stdin.readline().split())
    node = {}
    children = {i: [] for i in range(n)}
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        children[u].append(v)
        children[v].append(u)

    dp = [[[0] * (2**20)] * n]
    for i in range(1, n+1):
        for j in range(2**20):
            for k in range(min(i+1, k)+1):
                if k == 1:
                    dp[i][j][k] = count_nodes(i-1, j, k)
                else:
                    dp[i][j][k] = sum([dp[child][xor_val][k-1] for child in children[i]])

    result = []
    for i in range(2**20):
        if all(dp[n-1][i][k] == 0 or dp[n-1][i][k] == k-1 for k in range(k+1)):
            result.append("YES")
        else:
            result.append("NO")

    print(*result, sep='\n')

solve()
