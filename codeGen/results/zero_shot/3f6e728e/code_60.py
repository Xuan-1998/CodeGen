import sys

def read_input():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        U = list(map(int, sys.stdin.readline().split()))
        L = list(map(int, sys.stdin.readline().split()))
        U.sort()
        L.sort()
        result = [0] * (C + 1)
        for i in range(1, C + 1):
            # TO DO: count the number of ways to build a sequence with length i
            pass
        print(' '.join(map(str, result)))

read_input()
