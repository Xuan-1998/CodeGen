code
k = int(input())
dp = {(0, 0): 1, (0, 1): 1}
for i in range(k):
    dp[(1, 0)] = dp.get((0, 0), 0) + dp.get((0, 1), 0)
    dp[(1, 1)] = dp.get((0, 0), 0) + dp.get((0, 1), 0)

n = int(input())
count = 0
for _ in range(n):
    bit = int(input())
    if bit & (1 << i):  # Check if the bit is set
        count += dp[(bit & (1 << i), bit & (1 << i))]
    else:
        count += dp.get((0, 0), 0) + dp.get((0, 1), 0)
print(count % (10**9 + 7))
