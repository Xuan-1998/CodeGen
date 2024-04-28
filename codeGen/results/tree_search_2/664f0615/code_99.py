from sys import stdin

def calculate_max_length(initial_speed, final_speed, time, max_change):
    memo = {(0, 0): 0}

    for second in range(1, time + 1):
        for prev_second in range(second - 1, -1, -1):
            if (prev_second, max_change) not in memo:
                continue
            if initial_speed <= final_speed and abs(final_speed - initial_speed) > max_change or second == time:
                break
            speed = (initial_speed + final_speed) // 2
            memo[(second, max_change)] = min(memo.get((prev_second, max_change), prev_second) + abs(speed - initial_speed), memo.get((prev_second, max_change), prev_second))
    
    return memo[(time, max_change)]

def main():
    line1 = list(map(int, stdin.readline().strip().split()))
    line2 = list(map(int, stdin.readline().strip().split()))

    print(calculate_max_length(*line1, *line2))

if __name__ == "__main__":
    main()
