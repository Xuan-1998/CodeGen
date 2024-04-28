def solve():
    initial_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    memo = {}

    def dfs(t, dv):
        if (t, dv) in memo:
            return memo[(t, dv)]
        
        if t == 0:
            return 0
        
        if dv < 0 or dv > max_change:
            return float('inf')

        left = (t - 1, dv - initial_speed)
        right = (t - 1, dv + final_speed)

        left_dist = dfs(*left) * abs(dv)
        right_dist = dfs(*right) * abs(dv)

        memo[(t, dv)] = max(left_dist, right_dist)

        return memo[(t, dv)]

    print(int(dfs(time, initial_speed)))

if __name__ == "__main__":
    solve()
