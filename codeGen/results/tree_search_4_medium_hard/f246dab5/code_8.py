import sys

n = int(input())
dp = [(0, 0)]  # base case: no trips made yet

for _ in range(n):
    t = int(input())
    last_minutes_left, last_cost = dp[-1]
    
    # calculate the minimum cost for this trip considering all possible ticket combinations
    one_trip_cost = min(last_cost + 20, last_cost + 50, last_cost + 120)
    
    if last_minutes_left - 1 >= 140:  # one day ticket can be used
        dp.append((0, one_trip_cost))
    elif last_minutes_left - 1 >= 90:  # 90 minute ticket can be used
        dp.append((last_minutes_left - 90, one_trip_cost + 50))
    else:  # one trip ticket can be used
        dp.append((last_minutes_left - 1, one_trip_cost + 20))

print([cost for minutes_left, cost in dp])
