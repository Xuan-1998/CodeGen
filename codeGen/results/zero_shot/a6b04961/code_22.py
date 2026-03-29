import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Sort edges by their end points
    edges.sort()

    # Initialize dp array
    dp = [0] * (n + 1)

    max_beauty = 0
    for i in range(n):
        for j in range(i+1):
            if edges[j][1] == i:
                break
        else:
            continue

        for k in range(j, n):
            if edges[k][0] == i:
                break
        else:
            continue

        # Calculate the beauty of this tail
        beauty = (k - j + 1) * (i - j)
        max_beauty = max(max_beauty, beauty)

    print(max_beauty)

if __name__ == "__main__":
    solve()
