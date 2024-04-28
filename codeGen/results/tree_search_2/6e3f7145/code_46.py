def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    start_index = 0
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if j-i+1 > max_length:
                    max_length = j-i+1
                    start_index = i
    
    return s[start_index:start_index+max_length]

if __name__ == "__main__":
    s = input()
    print(longest_palindromic_substring(s))
