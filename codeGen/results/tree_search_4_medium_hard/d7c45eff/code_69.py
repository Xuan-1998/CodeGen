def find_smallest_string(n, k):
    dp = [['' for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        if i == 0:
            continue
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j] = ''
            elif j < i-1:
                dp[i][j] = min(dp[i-1][j], s[:i-1]+s[-1:][0]) if s else ''
            else:
                dp[i][j] = min(dp[i-1][j-1], s+s[-1:][0])
    
    return dp[n][k]

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(find_smallest_string(n, k))
