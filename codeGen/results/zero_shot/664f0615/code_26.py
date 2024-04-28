s1, s2 = map(int, input().split())
t, d = map(int, input().split())

max_speed = max(s1, s2)
min_speed = min(s1, s2)

print(min(d, (max_speed - min_speed) // d * t))
