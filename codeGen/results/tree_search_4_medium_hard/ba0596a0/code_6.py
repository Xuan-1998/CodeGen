from typing import List

def can_cross_stones(stones: List[int]) -> bool:
    n = len(stones)
    dp = [[False for _ in range(max(stones) + 1)] for _ in range(n)]

    dp[0][0] = True
    for i in range(1, n):
        for d in range(max(stones[i - 1], stones[i]) + 2):
            if (d - 1 >= stones[i - 1] and dp[i - 1][d - 1]):
                dp[i][d - 1] = True
            if (d == stones[i - 1] or d - 1 <= stones[i - 1] or dp[i - 1][d - 2]):
                dp[i][d] = True
            if (d + 1 <= stones[i] and dp[i - 1][d]):
                dp[i][d + 1] = True

    return dp[-1][-1]

if __name__ == "__main__":
    stones = list(map(int, input().split()))
    print(can_cross_stones(stones))
