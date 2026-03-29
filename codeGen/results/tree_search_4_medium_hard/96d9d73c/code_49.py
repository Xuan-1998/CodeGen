from sys import stdin
read = lambda: map(int, stdin.readline().split())

N, K, M = read()
A = [int(x) for x in stdin.read().split()]

dp = {(0, 1): True}

for i in range(1, N+1):
    for j in range(min(K, i+1), 0, -1):
        dp[(i, j)] = (dp.get((i-1, j-1), False) and abs(A[i] - A[i-1]) <= M)

print(dp.get((N, K), False))
