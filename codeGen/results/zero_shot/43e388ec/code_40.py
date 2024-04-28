a, b = map(int, input().split())
ans = 0
for i in range(314160):
    if i & (i-1) == 0: 
        ans += ((a << i) ^ b) % (10**9 + 7)
print(ans)
