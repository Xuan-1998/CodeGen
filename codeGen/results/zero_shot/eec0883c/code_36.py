from collections import deque

def solve():
    n = int(input())
    gasolines = list(map(int, input().split()))
    roads = []
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        roads.append((u, v, c))

    visited = [False] * (n+1)
    max_gasoline = 0

    for i in range(1, n+1):
        if not visited[i]:
            q = deque([(i, gasolines[i-1])])
            while q:
                city, remaining_gasoline = q.popleft()
                visited[city] = True
                for road in roads:
                    if road[0] == city and not visited[road[1]]:
                        q.append((road[1], min(remaining_gasoline + road[2], gasolines[road[1]-1]))))
                    elif road[1] == city and not visited[road[0]]:
                        q.append((road[0], min(remaining_gasoline - road[2], gasolines[road[0]-1]))))
                max_gasoline = max(max_gasoline, remaining_gasoline)

    print(max_gasoline)

if __name__ == "__main__":
    solve()
