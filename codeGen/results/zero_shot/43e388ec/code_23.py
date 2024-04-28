a = int(input(), 2)
b = int(input(), 2)

ans = sum(((a ^ (b << i)) % (10**9 + 7)) for i in range(314159))

print(ans)
