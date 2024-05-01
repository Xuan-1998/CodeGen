a, b = map(int, input().split())
cum_sum = 0
for i in range(314160):
    cum_sum = (cum_sum + ((a >> i) | (b << (i & 1)))) % (10**9+7)
print(cum_sum)
