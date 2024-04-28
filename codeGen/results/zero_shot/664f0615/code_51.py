v1, v2 = map(int, input().split())
t, d = map(int, input().split())

max_length = 0
for i in range(t):
    max_length += min(v2 - v1, d // (i + 1))
    if i < t - 1:
        v1 += min(v2 - v1, d // (i + 1))
print(max_length)
