import sys
input()
n = int(input())
p = 1
for i in range(1, n+1):
    p = (p * 0.5) % 998244353
print(p)
