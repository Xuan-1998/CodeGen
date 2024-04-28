a = int(input(), 2)
b = int(input(), 2)

sum_xor_shift = 0
for i in range(314160):
    b <<= 1
    sum_xor_shift += a ^ b
    a %= 10**9 + 7
    b %= 10**9 + 7

print(sum_xor_shift % (10**9 + 7))
