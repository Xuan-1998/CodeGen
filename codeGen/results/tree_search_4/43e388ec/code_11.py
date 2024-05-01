def solve():
    a, b = map(int, input().split())
    dp = [a ^ b]
    for i in range(1, 316):
        dp.append(dp[-1] ^ (b << i))
    print(sum(dp) % (10**9 + 7))

solve()
