def min_mana_required(input):
    n = int(input.readline())  # number of monsters
    appearances = list(map(int, input.readline().split()))  # appearance times
    healths = list(map(int, input.readline().split()))  # monster healths

    dp = [0] * (max(appearances) + 1)
    for i in range(n):
        for t in range(appearances[i], -1, -1):  # iterate from current appearance time to the start of the level
            if t >= appearances[i]:
                dp[t] = max(dp[t], healths[i] + (t > 0 and dp[t-1]) or 0)  # update DP table

    return sum(dp)  # return the total mana required

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        t = int(f.readline())
        for _ in range(t):
            n, *appearances, *healths = [int(x) for x in f.read().split()]
            print(min_mana_required(n, appearances, healths))
