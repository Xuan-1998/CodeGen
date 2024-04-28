v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

max_len = 0
for i in range(v1, v2+1):
    max_len += min(dv, (v2 - i) / (t-1))

print(max_len)
