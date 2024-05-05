import sys

def read_input():
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    return n, k, h


def min_mana(k, h):
    dp = [sys.maxsize] * (max(k) + 1)
    for i in range(1, len(k)):
        prev_damage = min(dp[k[i-1]], h[i-1])
        dp[k[i]] = min(prev_damage + 1, h[i])

    return sum([dp[j] for j in k])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k, h = read_input()
        print(min_mana(k, h))
