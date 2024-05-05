import sys

# Read input
T = int(sys.stdin.readline())
for _ in range(T):
    N, M, C = map(int, sys.stdin.readline().split())
    U = list(map(int, sys.stdin.readline().split()))
    L = list(map(int, sys.stdin.readline().split()))

    # Count the number of spheres with each radius
    counts = [0] * (C + 1)
    for r in U:
        counts[r] += 1
    for r in L:
        counts[r] += 1

    # Calculate the number of ways to build an i-sequence
    ans = [0] * C
    for i in range(C):
        ans[i] = (ans[i-1] if i > 0 else 1) + counts[i]
        ans[i] %= 10**9 + 7

    # Print the answer
    print(' '.join(map(str, ans)))
