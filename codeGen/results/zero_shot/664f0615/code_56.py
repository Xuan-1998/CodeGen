v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

speeds = [v1]
current_speed = v1
for _ in range(t-1):
    current_speed = min(max(current_speed + dv, v1), v2)
    speeds.append(current_speed)

print(sum((v - v1) / (dv or 1) for v in speeds))
