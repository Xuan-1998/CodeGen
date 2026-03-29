import sys

def solve(n, k):
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    # base case: strings of length 0 are always an empty string
    for i in range(n+1):
        dp[i][0] = ['']

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j == 0:
                # only one possible string of length 0: the empty string
                dp[i][j] = [dp[i-1][j][0]]
            elif j < i:
                # consider all possible strings of length j-1 and add a character to the end or duplicate them
                temp = []
                for s in dp[i-1][j]:
                    temp.append(s + (chr(ord('a') + j) if len(s) < j else ''))
                    temp.append(s * 2)
                dp[i][j] = sorted(temp)
            else:
                # consider all possible strings of length i-1 and add a character to the end or duplicate them
                temp = []
                for s in dp[i-1][k]:
                    temp.append(s + (chr(ord('a') + k) if len(s) < k else ''))
                    temp.append(s * 2)
                dp[i][j] = sorted(temp)

    # return the lexicographically smallest string of length k
    return dp[n][k][0]

n, k = map(int, input().split())
print(solve(n, k))
