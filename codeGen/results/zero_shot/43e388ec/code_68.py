a = int(input(), 2)
b = int(input(), 2)

sum_ = 0
for i in range(314160):
    if (a & (1 << i)) and ((b >> i) & 1):
        sum_ = (sum_ + 1) % (10**9 + 7)
    elif not (a & (1 << i)) and not ((b >> i) & 1):
        sum_ = (sum_ + 0) % (10**9 + 7)

print(sum_)
