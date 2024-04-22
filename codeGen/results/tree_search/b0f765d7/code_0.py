import sys

def read_int():
    return int(sys.stdin.readline().strip())

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def vitamin_mask(vitamins):
    mask = 0
    for v in vitamins:
        if v == 'A':
            mask |= 1
        elif v == 'B':
            mask |= 2
        elif v == 'C':
            mask |= 4
    return mask

n = read_int()
dp = [float('inf')] * 8
dp[0] = 0

for _ in range(n):
    price, vitamins = sys.stdin.readline().strip().split()
    price = int(price)
    mask = vitamin_mask(vitamins)
    for i in range(8):
        combined_mask = i | mask
        dp[combined_mask] = min(dp[combined_mask], dp[i] + price)

if dp[7] == float('inf'):
    print(-1)
else:
    print(dp[7])
