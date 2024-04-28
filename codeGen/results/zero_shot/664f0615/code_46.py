s0, s1 = map(int, input().split())
t, v = map(int, input().split())

max_length = 0
for i in range(t):
    if i == 0:
        max_length += (s1 - s0) // v * t + min((s1 - s0) % v, v)
    elif i == t-1:
        max_length += (s1 - s0) // v * t + min((s1 - s0) % v, v)
    else:
        if i == 1:
            max_length += min(s1 - s0, v)
        else:
            max_length += v
print(max_length)
