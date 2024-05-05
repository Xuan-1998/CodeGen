===BEGIN SOLUTION===
import math

def main():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        upper_radii = list(map(int, input().split()))
        lower_radii = list(map(int, input().split()))

        dp = [0] * (C + 1)
        dp[1] = 1

        for i in range(2, C + 1):
            if i not in C_count:
                C_count[i] = 0
            dp[i] = sum(dp[j] * math.comb(C_count[C_index].index(j), C_count[C_index][j]) for j in range(1, i + 1))

        print(*[dp[i] % (10**9 + 7) for i in range(1, C + 1)], sep=' ')

main()
