code
from sys import stdin, stdout

initial_speed, final_speed = map(int, stdin.readline().split())
time, max_allowed_change = map(int, stdin.readline().split())

dp = [(0, 0)]  # Initialize the dp array with the initial state
for _ in range(time):
    new_dp = []
    for speed_diff, time in dp:
        if abs(speed_diff - max_allowed_change) <= final_speed - initial_speed:
            new_dp.append((speed_diff + min(final_speed, initial_speed + speed_diff), time + 1))
    dp = new_dp

max_length = 0
for _, time in dp:
    max_length = max(max_length, (time - 1) * (final_speed + initial_speed) // 2)

stdout.write(str(max_length) + '\n')
