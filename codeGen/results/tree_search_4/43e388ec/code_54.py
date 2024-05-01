import sys

a, b = map(int, input().split())
ans = ((a ^ b) % (10**9 + 7))

for i in range(1, 314159):
    ans = ((ans ^ (b >> i%31)) % (10**9 + 7))
    
print(ans)
