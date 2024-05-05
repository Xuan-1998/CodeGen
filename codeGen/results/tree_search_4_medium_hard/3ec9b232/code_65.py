from collections import Counter

def count_partitions(n):
    M = list(map(int, input().split()))
    counter = Counter(M)
    cum = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        cum[i][0] = 1
        for j in range(1, min(i, max(counter)) + 1):
            cum[i][j] = (cum[i - 1][j - 1] * counter[M[i - 1]] + cum[i - 1][j]) % (10**9 + 7)
    
    return cum[n][n]

print(count_partitions(int(input())))
