import sys
T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    result = []
    for i in range(1, X+1):
        if i % (M-1) == 0:
            result.append(i)
        else:
            result.append((i-1)%M + 1)
    print(' '.join(map(str, result)))
