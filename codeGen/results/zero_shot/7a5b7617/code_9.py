import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    result = 0
    for i in range(M+1):
        if (M+1)*i//2 <= N:
            j = min(N, (M+1)*i//2 - 1)
            result += pow(10, 9, 10**12) * binomial(N-1, j-1)
    print(result % 10**12)

def binomial(n, k):
    if k > n-k:
        k = n-k
    result = 1
    for i in range(k+1):
        result = result*(n-i)//i
    return result
