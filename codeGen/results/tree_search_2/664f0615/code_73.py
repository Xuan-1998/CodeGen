def solve():
    initial_speed, final_speed = map(int, input().split())
    time_left, allowed_change = map(int, input().split())

    max_length = 0
    for speed in range(initial_speed, final_speed + 1):
        length = dp(speed, time_left, allowed_change)
        if length > max_length:
            max_length = length

    print(max_length)

if __name__ == "__main__":
    solve()
