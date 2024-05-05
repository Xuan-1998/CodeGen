import sys

def can_frog_cross(stones):
    n = len(stones)
    dp = [False] * n

    for i in range(1, n):
        if stones[i] - stones[i-1] == 1:  # k-1 jump
            dp[i] = True
        elif i >= 2 and abs(stones[i] - stones[i-2]) in (1, 2):  # k or k+1 jump from previous two stones
            dp[i] = True

    return dp[-1]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    stones = list(map(int, sys.stdin.readline().split()))
    print(can_frog_cross(stones))
