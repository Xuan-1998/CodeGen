import sys

q = int(sys.stdin.readline())
dp = [0] * (2 ** 30)
dp[0] = 1

for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    while v > 0:
        if dp[v] == 1:
            print("YES")
            break
        v &= (v - 1)
    else:
        print("NO")
