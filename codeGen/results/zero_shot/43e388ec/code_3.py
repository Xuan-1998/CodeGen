a = int(input())
b = int(input())

result = 0
for i in range(314159):
    b_shifted = (b << i) % (10**9 + 7)
    x_or_b_shifted = a ^ b_shifted
    result = (result + x_or_b_shifted) % (10**9 + 7)

print(result)
