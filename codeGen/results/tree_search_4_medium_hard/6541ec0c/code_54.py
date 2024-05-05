def solve(n, k):
    # Initialize DP table with all 0s
    dp = [[[0] * (1 << 18) for _ in range(k + 1)] for _ in range(n + 1)]

    # Base case: single node
    dp[0][0][0] = 1

    # Fill up the first row (i=0)
    for j in range(1, k + 1):
        dp[0][j][0] = 0

    # Transition function
    def dfs(i, j, xor_val):
        if dp[i][j][xor_val]:
            return True

        for child in children[i]:
            if dfs(child, j - 1, (xor_val ^ node_values[child])):
                return True

        return False

    # Compute DP values
    for i in range(1, n + 1):
        children = []
        for child in range(i):
            if parent[child] == i:
                children.append(child)
        for j in range(k + 1):
            for xor_val in range(1 << 18):
                if dfs(i, j, xor_val):
                    dp[i][j][xor_val] = 1

    # Output
    if dp[n][k][0]:
        print("YES")
    else:
        print("NO")

# Read input
n, k = map(int, input().split())
node_values = list(map(int, input().split()))
parent = [int(x) for x in input().split()]

solve(n, k)
