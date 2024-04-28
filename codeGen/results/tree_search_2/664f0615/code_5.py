from functools import lru_cache

allowedSpeedChange = int(input())
time, initial_speed, final_speed = map(int, input().split())

@lru_cache(None)
def dp(i, speed):
    if i == 0: return 0
    time_at_speed = (i * 100) / speed
    if i > 1:
        allowed_faster = min(100, speed + allowedSpeedChange)
        allowed_slower = max(1, speed - allowedSpeedChange)
        dp_values = [
            dp(i-1, allowed_faster),
            dp(i-1, allowed_slower),
        ]
        return max(dp_values) + time_at_speed
    return 0

print(max((dp(i, initial_speed) for i in range(2, time+1))))
