import sys

def main():
    n, m = map(int, input().split())
    edges = [[*map(int, input().split())] for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))
    
    dp = [[[0, 0]]*(n+1) for _ in range(k+1)]
    
    for i in range(1, n+1):
        if edges[i-1][1] == path[0]:
            dp[0][i] = [1, 1]
    
    for j in range(1, k+1):
        prev_v = path[j-1]
        for v in range(1, n+1):
            if (edges[v-1][0] == prev_v or edges[v-1][1] == prev_v):
                min_rec, max_rec = dp[j-1][v]
                if j < k:
                    next_v = path[j]
                    for w in range(1, n+1):
                        if (edges[w-1][0] == next_v or edges[w-1][1] == next_v):
                            min_rec = min(min_rec, dp[j-1][w][0] + 1)
                            max_rec = max(max_rec, dp[j-1][w][1] + 1)
                dp[j][v] = [min_rec, max_rec]
    
    print(*dp[k][-1], sep=' ')

if __name__ == "__main__":
    main()
