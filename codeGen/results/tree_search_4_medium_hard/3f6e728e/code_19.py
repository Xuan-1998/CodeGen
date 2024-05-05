from math import comb

def solve():
    T = int(input())  # number of test cases
    for _ in range(T):
        N, M, C = map(int, input().split())  # N upper hemispheres and M lower hemispheres, each with a radius between 1 and C
        U_rads = list(map(int, input().split()))  # radii of the upper hemispheres
        L_rads = list(map(int, input().split()))  # radii of the lower hemispheres

        dp = [0] * (C + 1)  # number of ways to build an i-sequence
        dp[1] = 1

        prefix_sum = [0] * (C + 1)  # cumulative sum of dp[j] for j in range(1, i)

        L_count = {}  # count the frequency of each lower hemisphere radius
        for rad in L_rads:
            if rad not in L_count:
                L_count[rad] = 0
            L_count[rad] += 1

        for i in range(2, C + 1):
            prefix_sum[i] = sum(comb(L_count[L_index].get(i, 0), j) * 
                                 (dp[j-1] if j > 0 else 1) % (10**9 + 7) for j in range(1, i)) % (10**9 + 7)
            dp[i] = prefix_sum[i]

        print(*map(str, dp), sep=' ')
