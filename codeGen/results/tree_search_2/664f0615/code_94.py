def solve():
    init_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    dp = {(0, 0): 0}  # base case: no change in speed

    for t in range(1, time + 1):
        for change in range(-max_change, max_change + 1):
            if (t - 1, change) not in dp:
                continue
            if t == 1 or (t - 1, change) in dp:
                dp[(t, change)] = min(dp.get((t - 1, change), float('inf')), change * 2 + dp.get((t - 1, change), 0))
            else:
                dp[(t, change)] = min(dp.get((t - 1, change), float('inf')), change)

    max_length = 0
    for t in range(time):
        for c in range(-max_change, max_change + 1):
            if (time, c) not in dp:
                continue
            length = dp[(time, c)] + abs(final_speed - init_speed)
            max_length = max(max_length, length)

    print(max_length)

if __name__ == '__main__':
    solve()
