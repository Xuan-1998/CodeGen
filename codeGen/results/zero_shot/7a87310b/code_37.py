import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0
    for a in range(1, N+1):
        for d in range(a, N+1):
            if (a*d - ((N-a-d)*(N-a-d))) > 0:
                count += 1
    print(count)
