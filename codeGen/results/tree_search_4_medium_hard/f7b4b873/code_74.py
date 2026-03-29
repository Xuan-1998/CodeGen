from collections import deque

def partition_palindromes(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]
    partitions = []

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if S[i] == S[j] and (j-i < 2 or dp[i+1][j-1]):
                dp[i][j] = True

    queue = deque([(0, n)])
    while queue:
        start, end = queue.popleft()
        if start >= end:
            continue
        for i in range(start, end):
            if S[start] == S[end-1] and (end-start < 2 or dp[start+1][end-2]):
                partition = [S[start:end+1]]
                queue.append((end, start))
                yield from (partition,)
            else:
                break

    for _ in range(n):
        partitions.extend(next(partition_palindromes(S), []))

    return partitions
