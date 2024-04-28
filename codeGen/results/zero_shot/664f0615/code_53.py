v1, v2 = map(int, input().split())
t, d = map(int, input().split())

speed_change_limit = abs(v2 - v1) // (t-1)
max_length = min((d * (v2 + v1)) / 2, (t - 1) * speed_change_limit)

print(max_length)
