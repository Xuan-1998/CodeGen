a = int(input())
b = int(input())

ans = 0
for i in range(314159):
    b_shift = (b << i) & ((1 << 30) - 1)
    xor_result = a ^ b_shift
    ans += xor_result
print(ans % (10**9 + 7))
