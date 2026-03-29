code = """
import sys

n = int(input())
portals = [int(x) for x in input().split()]

dp = {(1, False): 0}
for i in range(2, n+2):
    dp[(i, False)] = float('inf')
    dp[(i, True)] = float('inf')
    for p in portals:
        if p < i and (p % 2 == 0) ^ (i-1) % 2:  # Check the portal type
            dp[(i, False)] = min(dp[(i, False)], dp[(p, False)] + 1)
        if p < i and (p % 2 != 0) ^ (i-1) % 2:
            dp[(i, True)] = min(dp[(i, True)], dp[(p, True)] + 1)

print(min(dp[(n+1, False)], dp[(n+1, True)]) % 1000000007)
