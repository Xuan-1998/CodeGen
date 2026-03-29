import sys

def check_ladder(n, m, queries):
    dp = [[False] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(m+1):
            if j > 0:
                if i <= queries[j-1][1]:
                    dp[i][j] = (dp[i-1][j-1] and (queries[j-1][1] - i + 1) >= 0)
                    
    result = []
    for query in queries:
        l, r = query
        if dp[r][m]:
            result.append("Yes")
        else:
            result.append("No")
    
    return "\n".join(result)

if __name__ == "__main__":
    n, m = map(int, input().split())
    queries = []
    for _ in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))
    print(check_ladder(n, m, queries))
