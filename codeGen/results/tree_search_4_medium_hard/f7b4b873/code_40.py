def partition_palindromes(s):
    n = len(s)
    dp = [[[] for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(i, -1, -1):
            if s[j] == s[i-1]:
                if i-j < 2:
                    dp[j][i].append([s[j:i+1]])
                else:
                    for k in range(j+1, i):
                        for p in dp[k][j]:
                            for q in dp[i-k-1][k+1]:
                                dp[j][i].append(p + [s[j:k+1]] + q)
            else:
                dp[j][i] = []
    
    return dp[0][n]

# Example usage
input_string = input()
print(partition_palindromes(input_string))
