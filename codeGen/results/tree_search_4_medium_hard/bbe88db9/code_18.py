def get_portals(n, portals):
    dp = [[0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    def dfs(room, crosses):
        if room == n + 1:
            return 0
        if visited[room]:
            return dp[room][crosses]
        visited[room] = True
        if crosses % 2 == 0:
            next_room = portals[room - 1] if room > 1 else n + 1
            dp[room][crosses] = dfs(next_room, crosses) + 1
        else:
            dp[room][crosses] = min(dfs(room - 1, 0) + 1, dfs(portals[room - 1], crosses + 1))
        return dp[room][crosses]
    print((dfs(1, 0)) % (10**9 + 7))

if __name__ == "__main__":
    n = int(input())
    portals = list(map(int, input().split()))
    get_portals(n, portals)
