import sys
from collections import Counter

T = int(input())

for _ in range(T):
    N, M, C = map(int, input().split())
    U_radii = list(map(int, input().split()))
    L_radii = list(map(int, input().split()))

    # Sort radii in ascending order
    U_radii.sort()
    L_radii.sort()

    # Initialize counters for upper and lower hemispheres
    u_counter = Counter(U_radii)
    l_counter = Counter(L_radii)

    # Initialize the result array with C elements, all set to 0
    res = [0] * (C + 1)

    # Iterate through the radii and count the number of sequences that can be built
    for i in range(1, C + 1):
        res[i] = (res[i - 1] + u_counter[i]) % (10**9 + 7)
        res[i] += l_counter.get(i, 0) % (10**9 + 7)

    # Print the result array
    print(*res, sep=' ')
