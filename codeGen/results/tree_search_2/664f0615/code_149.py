from sys import stdin

def max_path_length(init_speed, final_speed, time, max_change):
    dp = [0] * 201  # Create a table for each possible speed difference
    dp[init_speed - init_speed] = 1  # Base case: the initial state is valid
    
    for _ in range(time):  
        new_dp = [0] * 201  # Create a new table to store intermediate results
        for i in range(201):
            if i <= max_change:
                dp[i] += dp[-i - 1]
            if i >= -max_change:
                dp[i] += dp[199 - i]
        dp = new_dp
    
    return sum(i * (dp[i] + dp[-i - 1]) // 2 for i in range(201) if i % 2 == 0 and i <= max_change)

if __name__ == "__main__":
    init_speed, final_speed = map(int, stdin.readline().split())
    time, max_change = map(int, stdin.readline().split())
    
    print(max_path_length(init_speed, final_speed, time, max_change))
