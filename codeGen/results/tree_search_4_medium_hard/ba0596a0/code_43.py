import sys

def can_cross(stones):
    dp = [False] * (len(stones) + 1)
    dp[0] = True

    for i in range(1, len(stones)):
        if not dp[i]:
            continue
        for j in range(max(0, stones[i] - 2), stones[i] + 3):
            if dp[j]:
                dp[i+1] = True
                break

    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    stones = list(map(int, input().split()))
    print(can_cross(stones))
