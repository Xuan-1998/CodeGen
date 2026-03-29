import sys

def infinite_zoo():
    n = int(input())
    dp = [False] * (1 << 30)
    dp[0] = True  # starting vertex is always reachable

    for _ in range(n):
        u, v = map(int, input().split())
        while v > 0:
            v &= u
        if not dp[u]:
            continue
        dp[v] = True

    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        print("YES" if dp[v] else "NO")

if __name__ == "__main__":
    infinite_zoo()
