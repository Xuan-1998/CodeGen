a = int(input())
b = int(input())

ans = 0
for i in range(314160):
    ans += (a^((b<<i)%1000000007))%1000000007

print(ans)
