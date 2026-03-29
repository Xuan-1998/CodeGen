def solve(n, k):
    memo = {(0, 0): True}  # base case: no edges

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if dp(i, j):
                result = (i, j)
                return "YES"
    return "NO"

def dp(i, j):
    state = {0: 0}  # initialize the subtree rooted at node i

    def dfs(u):
        val = u
        for v in range(1, n+1):
            if v != u:
                if (v, val) not in memo:
                    memo[(v, val)] = dfs(v)
                val ^= memo[(v, val)]
        return val

    dfs(i)
    dfs(j)

    return all(val == state[i] for val in state.values())

n, k = map(int, input().split())
print("YES" if solve(n, k) else "NO")
