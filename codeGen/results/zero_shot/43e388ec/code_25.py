a, b = map(int, input().split())
sum_xor_shift = 0
for i in range(314160):
    temp = a ^ (b << i)
    sum_xor_shift = (sum_xor_shift + temp) % (10**9 + 7)
print(sum_xor_shift)
