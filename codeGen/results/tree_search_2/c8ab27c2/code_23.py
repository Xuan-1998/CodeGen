def findShortestSubArray(S, T):
    m = [[0, 0, float('inf')] for _ in range(len(T) + 1)]
    for i, (a, b) in enumerate(zip(S, T)):
        if a == b:
            if i > 0 and m[i-1][2] < i - m[i-1][1]:
                m[i] = [i-1, i, i]
            else:
                m[i] = [m[i-1][2], i, i]

    return min(m[i][2] - m[i][0] for i in range(len(T) + 1)) if any(m[i][2] < float('inf') for i in range(len(T) + 1)) else -1

import sys
input = lambda: map(int, input().split())
S, T = input(), input()
print(findShortestSubArray(S, T))
