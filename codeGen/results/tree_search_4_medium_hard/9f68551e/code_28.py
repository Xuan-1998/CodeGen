import sys

def solve():
    n = int(input())
    k = [int(x) for x in input().split()]
    h = [int(x) for x in input().split()]

    dp = [0] * (max(k) + 1)
    prev_damage = float('inf')

    for j in range(max(k), 0, -1):
        if j == k[0]:
            dp[j] = min(prev_damage + 1, h[0])
        else:
            i = k.index(j)
            dp[j] = min(prev_damage + 1, h[i])
        prev_damage = dp[j]

    print(min(dp))

if __name__ == "__main__":
    solve()
