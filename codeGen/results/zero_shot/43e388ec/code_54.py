a, b = map(int, input().split())
sum_xor_shift = 0
for i in range(314160):
    xor = a ^ (b << i)
    sum_xor_shift += xor
print(sum_xor_shift % (10**9 + 7))
