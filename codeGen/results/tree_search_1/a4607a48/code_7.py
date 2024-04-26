import sys

def floyd_warshall(dist, n, m):
    for k in range(n * m):
        for i in range(n * m):
            for j in range(n * m):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def main():
    n, m = map(int, input().split())
    universe = [input() for _ in range(n)]

    # Initialize the distance matrix
    dist = [[float('inf')] * (n * m) for _ in range(n * m)]

    # Set the distance between adjacent cells and self-loops
    for i in range(n):
        for j in range(m):
            if universe[i][j] == '.':
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and universe[ni][nj] == '.':
                        dist[i * m + j][ni * m + nj] = 1
                dist[i * m + j][i * m + j] = 0

    # Apply the Floyd-Warshall algorithm
    floyd_warshall(dist, n, m)

    # Calculate the sum of all shortest path distances
    total_distance = 0
    count = 0
    for i in range(n * m):
        for j in range(i + 1, n * m):
            if dist[i][j] != float('inf'):
                total_distance += dist[i][j]
                count += 1

    # Calculate the average lifespan
    average_lifespan = total_distance / count if count else 0
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
