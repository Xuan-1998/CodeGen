import sys

def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * n
    dp[0] = True  # base case: frog starts on the first stone

    for i in range(1, n):
        for j in range(max(0, i-k-1), min(i, k+1)):
            if dp[j]:
                dp[i] = True
                break

    return dp[-1]

k = int(input())  # input: distance of each jump
stones = [int(x) for x in input().split()]  # input: positions of stones

if can_cross_stones(stones):
    print("Yes")
else:
    print("No")
