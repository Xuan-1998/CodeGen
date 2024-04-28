import sys

def shortest_uncommon_subsequence():
    s = input().strip()
    t = input().strip()

    memo = {(0, 0): 0}

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                dp = min(memo.get((i-1, j), float('inf')), memo.get((i, j-1), float('inf')))
            else:
                dp = max(memo.get((i-1, j), 0), memo.get((i, j-1), 0))
            memo[(i, j)] = dp + 1

    return max(max(row) for row in memo.values()) if any(dp > 0 for dp in memo.values()) else -1

print(shortest_uncommon_subsequence())
