import sys

def find_max_gasoline():
    n = int(sys.stdin.readline())
    w = list(map(int, sys.stdin.readline().split()))
    roads = []
    for _ in range(n - 1):
        u, v, c = map(int, sys.stdin.readline().split())
        roads.append((u, v, c))

    max_gasoline = w[0]
    current_city = 0
    visited = [False] * n

    def dfs(city):
        nonlocal max_gasoline
        if not visited[city]:
            visited[city] = True
            for road in roads:
                if road[0] == city and not visited[road[1]]:
                    next_city, c = road[1], road[2]
                    gas_left = w[next_city] - c
                    if gas_left > max_gasoline:
                        max_gasoline = gas_left
                    dfs(next_city)

    dfs(0)
    print(max_gasoline)


if __name__ == "__main__":
    find_max_gasoline()
