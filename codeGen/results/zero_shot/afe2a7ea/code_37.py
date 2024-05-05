import sys
input = sys.stdin.readline

n = int(input())
prob = 1
for i in range(1, n):
    prob *= (2 * i) // i
print(prob % 998244353)
