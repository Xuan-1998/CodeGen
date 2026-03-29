from collections import defaultdict

def can_frog_cross(stones):
    dp = [False] * len(stones)
    dp[0] = True  # base case: frog starts on first stone

    for i in range(1, len(stones)):
        for j in range(max(0, i - 2), i):  # iterate over previous stones
            if dp[j]:  # if frog can reach j from previous ones
                k = abs(stones[i] - stones[j])
                if k == 1 or k == 2:  # check valid jump distance
                    dp[i] = True
                    break

    return dp[-1]

if __name__ == "__main__":
    stones = [int(x) for x in input().split()]
    print(can_frog_cross(stones))
