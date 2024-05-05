import sys
input = sys.stdin.readline

def solve(N, M, C):
    # Sort the radii in ascending order
    upper_radii = sorted([int(x) for x in input().split()])
    lower_radii = sorted([int(x) for x in input().split()])

    # Initialize the count array
    counts = [0] * (C + 1)

    # Count the number of ways to build an i-sequence
    for r in upper_radii:
        for i in range(r, C + 1):
            counts[i] += 1
    for r in lower_radii:
        for i in range(1, r + 1):
            counts[i] -= 1

    # Calculate the number of ways to build an i-sequence modulo 10^9+7
    result = [0] * (C + 1)
    result[0] = 1
    for i in range(1, C + 1):
        result[i] = (result[i - 1] * (counts[i] + 1)) % (10**9 + 7)

    return ' '.join(map(str, result))

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    print(solve(N, M, C))
