import sys
from collections import defaultdict

def process_queries(signs, queries):
    n = len(signs)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        if signs[i-1] == '+':
            dp[i][i] = 1
        else:
            dp[i][i] = -1
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if signs[i] == signs[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1])
    
    results = []
    for l, r in queries:
        results.append(min(dp[l][r]))
    
    return results

def main():
    n = int(input())
    signs = input()
    queries = [list(map(int, input().split())) for _ in range(int(input()))]
    results = process_queries(signs, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
