from collections import defaultdict

def max_length_segment():
    memo = defaultdict(int)
    
    def dfs(time, initial_speed, final_speed):
        if (time, initial_speed) not in memo:
            if time == 1:
                return min(initial_speed, final_speed)
            else:
                for speed in range(min(initial_speed, final_speed), max(initial_speed, final_speed) + 1):
                    if abs(speed - initial_speed) <= max_change and abs(speed - final_speed) <= max_change:
                        memo[(time, initial_speed)] = speed
                        break
                return dfs(time - 1, speed, final_speed)
        return memo[(time, initial_speed)]
    
    initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]
    print(dfs(time, initial_speed, final_speed))
