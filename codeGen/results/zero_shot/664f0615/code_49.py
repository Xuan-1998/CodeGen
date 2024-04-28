v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

max_length = 0
speed_diff = abs(v2 - v1)
for i in range(t):
    if i == 0:
        length = (dv * speed_diff) / (2 * v1)
    elif i == t - 1:
        length = (dv * speed_diff) / (2 * v2)
    else:
        length = dv
    max_length = max(max_length, length)

print(int(max_length))
