import math

n = int(input())
prob = 1
for i in range(n.bit_length()):
    prob *= (1 << i) % 998244353
print(prob)
