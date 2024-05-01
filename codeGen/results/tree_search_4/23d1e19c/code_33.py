import sys

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    k = int(input())
    path = list(map(int, input().split()))

    min_dp = [float('inf')] * (n+1); 
    min_dp[1] = (0, 0);
    max_dp = [float('-inf')] * (n+1); 
    max_dp[1] = (0, 0);

    for i in range(2, n+1):
        if path[i-1] == path[-1]:
            min_dp[i] = min(min_dp[i-1][0]+1, k), max(max_dp[i-1][1], k)
            max_dp[i] = (min_dp[i][0], max_dp[i][1])
        else:
            min_dp[i] = min(min_dp[i-1][0]+1, 1), max(max_dp[i-1][1], 1)
            max_dp[i] = (min_dp[i][0], max_dp[i][1])

    print(*min_dp[-1], sep=' ')
    print(*max_dp[-1], sep=' ')

if __name__ == "__main__":
    main()
