t, l, r = map(int, input().split())
ans = ((sum(range(t+1)) - l*(r-l+1)) % (10**9 + 7))
print(ans)
