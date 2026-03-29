def lexicographically_smallest_string(n, k):
    s = input()
    
    dp = [[s[:i]] + [''] * (k - i) for i in range(k+1)]
    
    for j in range(1, k+1):
        if j == 1:
            dp[k][j-1] = s[:k]
        else:
            for i in range(min(j, n), 0, -1):
                if s[n-i+1] <= s[n-j]:
                    dp[k][j-1] = (s[n-j:n-i+1] + dp[k-1][j-1]) if j > 1 else s[:k]
                    break
                elif i == 1:
                    dp[k][j-1] = s[:n-j+1]
    
    return dp[k][j-1]

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(lexicographically_smallest_string(n, k))
