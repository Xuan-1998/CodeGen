def partition_palindromes(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 0 if length == 2 else dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
    
    def backtrack(i, j):
        if i > j:
            return [""]
        if dp[i][j] == 0:
            return [[s[i:j+1]]]
        result = []
        for k in range(i, j + 1):
            left_partitions = backtrack(i, k - 1)
            right_partitions = backtrack(k + 1, j)
            for lp in left_partitions:
                for rp in right_partitions:
                    if lp and rp:
                        result.append([lp[0], s[k]] + rp)
                    else:
                        result.append([s[i:k+1]] + (rp or [s[k:j+1]]))
        return result
    
    return backtrack(0, n - 1)

import sys

if __name__ == "__main__":
    S = sys.stdin.read().strip()
    print(partition_palindromes(S))
