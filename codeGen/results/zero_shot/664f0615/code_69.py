v0, v1 = map(int, input().split())
t, delta = map(int, input().split())

max_length = 0
for i in range(v0, v1+1):
    max_length += min(i + delta, t) - (i > 0)
print(max_length)
