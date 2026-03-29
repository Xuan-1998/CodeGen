def solve():
    q = int(input())  # Read the number of queries
    dp = [[0] * (2 ** 30) for _ in range(2 ** 30)]  # Initialize the DP table

    for i in range(q):
        u, v = map(int, input().split())  # Read a query (u, v)
        if u == v:  # Base case: path exists when u equals v
            print("YES")
        else:
            found = False
            for w in range(2 ** 30):  # Try to find a w such that (u & w) = w
                if (u & w) == w and dp[w][v]:  # If a path exists from w to v
                    print("YES")
                    found = True
                    break
            if not found:  # If no path is found, return "NO"
                print("NO")

solve()
