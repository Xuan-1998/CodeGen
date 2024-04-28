v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

speed_range = range(min(v1, v2), max(v1, v2) + 1)
max_length = 0

for speed in speed_range:
    length = (v2 - speed) * t / dv
    max_length = max(max_length, int(length))

print(max_length)
