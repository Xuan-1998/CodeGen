def min_cuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the first row as True, because single-character strings are always palindromes.
    for i in range(n):
        dp[i][i] = True
    
    count = 0
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if the substring is palindromic.
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
            else:
                count += 1
    
    return count

def main():
    s = input()
    
    print(min_cuts(s))

if __name__ == "__main__":
    main()
