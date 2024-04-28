import sys

def solve():
    initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]
    
    dp = {}
    max_length = 0
    
    for i in range(time):
        if i == 0:
            speed = initial_speed
        elif i == time - 1:
            speed = final_speed
        else:
            if (i, abs(final_speed - initial_speed)) not in dp:
                dp[(i, abs(final_speed - initial_speed))] = min(final_speed, initial_speed) + max_change * (i > 0)
            speed = dp.get((i, abs(final_speed - initial_speed)), i * min(initial_speed, final_speed))
        
        if i == time - 1:
            max_length += abs(speed - final_speed)
        else:
            max_length += abs(speed - min(final_speed, initial_speed)) + (time - 1 - i) * min(final_speed, initial_speed)
    
    print(max_length)

if __name__ == "__main__":
    solve()
