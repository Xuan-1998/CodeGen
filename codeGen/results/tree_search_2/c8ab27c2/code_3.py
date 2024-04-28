import sys

def shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    dp = [[False] * (len(T) + 1) for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = False

    max_length = -1
    for length in range(1, len(S) + 1):
        for i in range(len(S) - length + 1):
            subsequence = S[i:i+length]
            found = True
            j = 0
            while j < len(T) and found:
                if T[j:j+length] == subsequence:
                    found = False
                j += 1
            if not found:
                max_length = length
                break

    print(max_length)

shortest_uncommon_subsequence()
