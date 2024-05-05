import sys

def solve(n, k, edges):
    memo = {}

    def dfs(node):
        if node not in memo:
            children = [edge[1] for edge in edges if edge[0] == node]
            xor_val = 0
            for child in children:
                xor_val ^= dfs(child)
            memo[node] = (xor_val, len(children) <= k - 1)

        return memo[node]

    result = []
    for i in range(n):
        if i not in memo:
            result.append("YES" if dfs(i)[1] else "NO")
        else:
            result.append("YES" if memo[i][1] else "NO")

    return "\n".join(result)

if __name__ == "__main__":
    input = sys.stdin.read().split("\n")
    n_tests = int(input[0])
    for _ in range(n_tests):
        n, k = map(int, input[_+1].split())
        edges = [(int(i), j) for i, line in enumerate(input[_+2:]) if (j := int(line)) != 0]
        print(solve(n, k, edges))
