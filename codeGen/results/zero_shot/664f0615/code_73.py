v0, v1, t, dv = map(int, input().split())
max_len = (t-1) * dv + abs(v0-v1)
print(max_len)
