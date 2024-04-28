from collections import defaultdict

def find_shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    memo = defaultdict(dict)

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            return -1

        if S[i-1] not in T[:j]:
            return dp(i-1, j) + 1
        else:
            return -1

    for i in range(1, len(S)+1):
        for j in range(1, len(T)+1):
            memo[(i, j)] = dp(i, j)

    shortest_uncommon_subsequence_length = float('inf')
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] != T[j]:
                if dp(i+1, j+1) == -1:
                    shortest_uncommon_subsequence_length = min(shortest_uncommon_subsequence_length, i+1)

    print(shortest_uncommon_subsequence_length if shortest_uncommon_subsequence_length != float('inf') else -1)
