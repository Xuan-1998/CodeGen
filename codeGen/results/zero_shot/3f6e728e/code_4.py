import sys

# Read input from stdin
T = int(sys.stdin.readline())
for _ in range(T):
    N, M, C = map(int, sys.stdin.readline().split())
    U = list(map(int, sys.stdin.readline().split()))
    L = list(map(int, sys.stdin.readline().split()))

    # Sort the hemispheres by radius
    U.sort()
    L.sort()

    # Initialize a dictionary to store the number of X-sequences for each length
    dp = {0: 1}

    # Iterate through the upper and lower hemispheres
    for u, l in zip(U, L):
        # For each length, find the maximum previous length that is less than or equal to the current length plus one
        for i in range(len(dp)):
            if i + 1 <= len(str(u)) + len(str(l)):
                dp[i+1] = (dp.get(i+1, 0) + dp[i]) % 1000000007

    # Print the number of X-sequences for each length
    print(' '.join(map(str, list(dp.values()))))
