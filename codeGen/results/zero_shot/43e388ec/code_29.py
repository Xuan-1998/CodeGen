a = int(input())
b = int(input())

result = 0
for i in range(314160):
    b_shifted = (b << i) % (10**9 + 7)
    result += a ^ b_shifted
    result %= (10**9 + 7)

print(result)
