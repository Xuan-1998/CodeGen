import sys

N = int(input())
str1 = input()
str2 = input()

dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

for len_ in range(1, N+1):
    for i in range(N+1-len_):
        for j in range(N+1-len_):
            k = i
            while k <= j and str1[i+len_-1] == str2[k+len_-1]:
                if len_ == 1:
                    dp[0][i][k][j] += 1
                else:
                    l = k
                    while l <= j and str1[i+len_-1] == str2[l+len_-1]:
                        l += 1
                    for x in range(k, l):
                        dp[len_][i][x][l-1] += dp[len_-1][i][k-1][x-1]
                k += 1

print(sum([sum(row) for row in dp[-1]]))
