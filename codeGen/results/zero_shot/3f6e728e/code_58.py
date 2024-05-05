import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        # Initialize the count of X-sequences
        count = 1

        # Iterate over the radii from 1 to C
        for i in range(1, C+1):
            # Count the number of upper hemispheres with radius i
            upper_count = sum(1 for u in U if u >= i)
            # Count the number of lower hemispheres with radius i
            lower_count = sum(1 for l in L if l >= i)

            # Calculate the number of X-sequences that can be built with radius i
            count *= (upper_count + 1) * (lower_count + 1)
            count %= 10**9 + 7

        print(*[str(count // (i+1)) for i in range(C, 0, -1)], sep=' ')

solve()
