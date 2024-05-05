import math

def solve(N, M):
    result = 0
    for i in range(M // N + 1):  # consider all possible sums for each row
        if i >= N:
            break  # no need to consider higher values
        for j in range(i + 1):  # fill up the rows with non-negative integers
            result += math.comb(N - 1, j) % (10 ** 9)
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))
