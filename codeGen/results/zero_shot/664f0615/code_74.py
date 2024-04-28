v0, v1 = map(int, input().split())
t, dv = map(int, input().split())

max_len = 0
for i in range(t):
    max_len += min((v1-v0)//dv * dv + dv, (v1-v0) * (i+1)) // (dv+1)

print(max_len)
