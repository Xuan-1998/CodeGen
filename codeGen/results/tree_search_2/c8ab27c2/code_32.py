import sys

def find_shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i-1] != T[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1]

    shortest_uncommon_subsequence_length = -1
    for i in range(1, len(S) + 1):
        if dp[i][0] > 0 and (shortest_uncommon_subsequence_length == -1 or dp[i][0] < shortest_uncommon_subsequence_length):
            shortest_uncommon_subsequence_length = dp[i][0]

    print(shortest_uncommon_subsequence_length)

if __name__ == "__main__":
    find_shortest_uncommon_subsequence()
