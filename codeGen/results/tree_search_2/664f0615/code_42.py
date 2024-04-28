import sys

def max_distance(initial_speed, final_speed, time, delta_speed):
    dp = {(0, 0): 0}  # base case: initial speed and time

    def transition(state):
        speed, time = state
        if time == time:
            return (final_speed, time)
        new_speed = min(max(speed + delta_speed, initial_speed), final_speed)
        return ((new_speed, time + 1) if new_speed != speed else state)

    for _ in range(time):
        dp.update({next_state: dp[state] + abs(next_speed - prev_speed) for state, (prev_speed, _) in dp.items() for next_state, next_speed in [(transition(state), next_speed) for state in [state for state in dp if state[1] == time-1]]})

    return max(dp.values(), key=lambda x: x)

initial_speed = int(input())
final_speed = int(input())
time = int(input())
delta_speed = int(input())

print(max_distance(initial_speed, final_speed, time, delta_speed))
