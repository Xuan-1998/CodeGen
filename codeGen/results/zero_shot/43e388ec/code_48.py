a = int(input(), 2)
b = int(input(), 2)

result = sum(((a^(1<<i))|(b<<(i+1))) for i in range(314159))
print(result % (10**9 + 7))
