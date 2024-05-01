code

a, b = map(int, input().split())
dp = a ^ b
total = dp
for i in range(1, 314160):
    temp = dp
    dp ^= (b * (2 ** i))
    total += (temp + dp) % (10**9 + 7)
print(total)
