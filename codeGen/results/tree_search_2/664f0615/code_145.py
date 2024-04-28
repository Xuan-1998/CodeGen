from collections import defaultdict

def dp(s, t):
    if s == 0 or t == 1:  # base case: all seconds exhausted or max change reached
        return t * abs(s - 0)  # maximum possible length is proportional to time

    memo = defaultdict(int)
    transitions = [(s + i, t - 1) for i in range(11)]  # generate next speeds within max change

    def dfs(speed):
        if speed not in memo:
            if speed == 0:  # reached the final speed
                return t
            elif speed > 100 or speed < 1:  # invalid speed
                return -float('inf')
            else:  # calculate and store the result for this speed
                results = []
                for next_speed in transitions:
                    if abs(next_speed[0] - speed) <= s:
                        results.append(1 + dp(next_speed[0], next_speed[1]))
                memo[speed] = max(results, default=-float('inf'))
        return memo[speed]

    return dfs(s)

# Read input from stdin
initial_speed, final_speed, time, max_change = map(int, input().split())

print(dp(initial_speed, time))
