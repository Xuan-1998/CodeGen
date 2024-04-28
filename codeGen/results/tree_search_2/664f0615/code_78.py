from sys import stdin

def solve():
    initial_speed, final_speed = map(int, stdin.readline().split())
    time, max_change = map(int, stdin.readline().split())

    memo = {}

    def dfs(speed):
        if speed in memo:
            return memo[speed]
        if speed == 0 or speed > final_speed:
            return 0
        if abs(final_speed - speed) <= max_change:
            return time
        min_length = float('inf')
        for _speed in range(max(1, speed-10), min(final_speed+1, speed+10)):
            length = dfs(_speed)
            if length < min_length:
                min_length = length + 1
        memo[speed] = min_length
        return min_length

    print(dfs(initial_speed))

if __name__ == "__main__":
    solve()
