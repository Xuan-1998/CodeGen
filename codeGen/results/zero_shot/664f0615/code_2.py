v0, v1 = map(int, input().split())
t, d = map(int, input().split())

max_acceleration = max_deceleration = min(abs(v1 - v0), d // t)

speeds = [v0]
for _ in range(t):
    speeds.append(speeds[-1] + (min(max_acceleration, 10) if _ < t - 1 else 0))

print(sum((speeds[i] + speeds[i+1]) * 0.5 for i in range(t)) * 100)
