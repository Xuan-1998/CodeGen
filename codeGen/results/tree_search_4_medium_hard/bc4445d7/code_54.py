def solve():
    n = int(input())
    k = 1
    for _ in range(n-1):
        u, v = map(int, input().split())
        # ... (compute edge label values and store them in a list)
        k *= product(edge_labels)

    memo = [0] * (n+1)
    memo[2] = 0

    def dfs(i):
        if i > n:
            return
        if memo[i] != 0:
            return memo[i]
        max_index = 0
        for j in range(2, i):
            index = dfs(j) + dfs(i-j) + k * (i-1)
            max_index = max(max_index, index)
        memo[i] = max_index
        return max_index

    print(dfs(n) % (10**9+7))

if __name__ == "__main__":
    solve()
