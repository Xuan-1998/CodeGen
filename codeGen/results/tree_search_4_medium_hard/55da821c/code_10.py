import sys

def solve():
    n, m = map(int, input().split())
    plants = [(int(s), float(x)) for s, x in (line.strip().split() for line in sys.stdin)]

    # Initialize state and memoization table
    state = {i: [0] * m for i in range(m)}
    memo = {}

    def dfs(i):
        if i >= n:
            return 0
        if (i, tuple(state[i])) in memo:
            return memo[(i, tuple(state[i]))]
        if plants[i][0] == state[i-1][plants[i-1][0]]:
            # Same species, continue filling the current section
            state[i][plants[i][0]] = state[i-1][plants[i-1][0]]
            return dfs(i+1)
        else:
            # Different species, start a new section
            min_replanted = float('inf')
            for j in range(m):
                if state[i-1][j] == 0:
                    state[i][plants[i][0]] = j + 1
                    replanted = dfs(i+1) + 1
                    min_replanted = min(min_replanted, replanted)
            return min_replanted

    # Initialize and compute the minimum number of replanted plants
    min_replanted = dfs(1)
    print(min_replanted)

if __name__ == "__main__":
    solve()
