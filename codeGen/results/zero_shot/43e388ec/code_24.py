a = int(input(), 2)
b = int(input(), 2)

total_sum = 0
for i in range(314159):
    total_sum += (a ^ ((b << i) & ((1 << (i+1)) - 1)))

print(total_sum % (10**9 + 7))
