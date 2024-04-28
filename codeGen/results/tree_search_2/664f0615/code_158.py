from sys import stdin

def max_distance(initial_speed, current_time, max_allowed_change):
    dp = {}
    
    def dfs(speed, time):
        if (speed, time) in dp:
            return dp[(speed, time)]
        
        if speed == initial_speed and time >= current_time:
            return 0
        
        if time < current_time:
            new_distance = 0
        else:
            new_distance = (time - current_time + 1) * speed
        
        max_dist = 0
        for next_speed in range(initial_speed, min(initial_speed + max_allowed_change, final_speed), -1):
            dist = dfs(next_speed, time - 1)
            if dist > max_dist:
                max_dist = dist
                new_distance = max_dist + (time - current_time) * speed
        
        dp[(speed, time)] = new_distance
        return new_distance
    
    initial_speed, final_speed, _, _ = [int(x) for x in stdin.readline().split()]
    _, time, _, _ = [int(x) for x in stdin.readline().split()]
    
    print(dfs(initial_speed, time))
