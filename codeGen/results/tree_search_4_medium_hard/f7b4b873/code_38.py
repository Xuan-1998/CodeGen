def partition_palindromes(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
    
    partitions = []
    def backtrack(i, j):
        if i > j:
            return [[]]
        result = []
        for partition in backtrack(i+1, j-1):
            if dp[i][j]:
                result.append([s[i:j+1]] + partition)
            else:
                result.extend([s[i]+part+s[j+1:] for part in partition])
        return result
    
    partitions = backtrack(0, n-1)
    
    return partitions

def main():
    s = input()
    print(partition_palindromes(s))

if __name__ == "__main__":
    main()

