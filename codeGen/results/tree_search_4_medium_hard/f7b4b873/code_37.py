def partition(s):
    dp = [[False] * len(s) for _ in range(len(s))]
    partitions = []

    for i in range(len(s)):
        dp[i][i] = True

    for length in range(2, len(s)+1):
        for i in range(len(s)-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (length == 2) or dp[i+1][j-1]
            else:
                dp[i][j] = False

    def backtrack(start, end, path=[]):
        if start > end:
            partitions.append(' '.join(path))
        for i in range(start, end+1):
            if dp[start][i]:
                backtracking = True
                for j in range(i, start-1, -1):
                    if s[j] != s[i-j+start]:
                        break
                else:
                    backtrack(i+1, end, path+[s[i-start:i+1]])
                    if i > start:
                        backtracking = False

    backtrack(0, len(s)-1)

    return partitions

n = int(input())
s = input().strip()
print(partition(s))
