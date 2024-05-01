import sys

def shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    dp = {}
    for i in range(len(S) + 1):
        for j in range(min(i, len(T)) + 1):
            if (i, j) not in dp:
                if i == 0 or j == 0:
                    dp[(i, j)] = 1
                elif S[i-1] != T[j-1]:
                    dp[(i, j)] = 1 + dp.get((i-1, j), 0)
                else:
                    dp[(i, j)] = dp.get((i-1, j-1), 0)

    return max(max(dp.values()))

print(shortest_uncommon_subsequence())
