a = int(input(), 2)
b = int(input(), 2)

result = [0] * (314160) 
for i in range(314160):
    result[i] = a ^ ((b << i) & ((1 << (i+1)) - 1))

print(sum(result) % (10**9 + 7))
