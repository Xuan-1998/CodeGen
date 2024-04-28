a = int(input(), 2)
b = int(input(), 2)

total_sum = 0
for i in range(314160):
    total_sum += (a ^ (b << i)) % (10**9 + 7)

print(total_sum)
