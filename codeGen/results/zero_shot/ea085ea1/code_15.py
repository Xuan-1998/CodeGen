import sys

def find_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[False] * (N+1) for _ in range(N+1)]

    max_count = 0

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = True
                max_count += 1

    return max_count

print(find_common_substrings())
