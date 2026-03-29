def solve():
    n = int(input())
    parent = list(map(int, input().split()))
    ranges = [list(map(int, input().split())) for _ in range(n)]

    memo = {}

    def dfs(node):
        if node not in memo:
            l, r = ranges[node-1]
            max_value = 0
            for child in range(2, n+1):
                if parent[child-1] == node:
                    max_value = max(max_value, dfs(child) + (r - l))
            memo[node] = max_value
        return memo[node]

    answer = 0
    for i in range(1, n+1):
        if i != 1:  # Root node
            answer += abs(ranges[i-1][1] - ranges[parent[i-1]][1])
    print(answer)

if __name__ == "__main__":
    solve()
