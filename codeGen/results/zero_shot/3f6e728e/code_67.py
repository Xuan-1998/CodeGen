def count_x_sequences():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N, M, C = map(int, input().split())  # Read N, M, and C
        U_radii = list(map(int, input().split()))  # Read radii of upper hemispheres
        L_radii = list(map(int, input().split()))  # Read radii of lower hemispheres

        # Initialize the dynamic programming table
        dp = [0] * (C + 1)
        dp[0] = 1  # Base case: one way to build an empty sequence

        # Fill in the dynamic programming table
        for i in range(1, C + 1):
            if U_radii:
                j = min(i, len(U_radii)) - 1
                while j >= 0 and U_radii[j] > i:
                    j -= 1
                dp[i] += sum(dp[:j+1])
            if L_radii:
                k = min(i, len(L_radii)) - 1
                while k >= 0 and L_radii[k] > i:
                    k -= 1
                dp[i] += sum(dp[:k+1])

        # Print the result
        print(' '.join(map(str, dp)))
