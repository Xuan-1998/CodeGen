def solve():
    v1, v2, t, delta = map(int, input().split())
    memo = {}

    def dp(time, max_change):
        if (time, max_change) in memo:
            return memo[(time, max_change)]
        
        if time == 0 or max_change == 0:
            return 0

        if time % 2 == 1:
            left_max = dp((time - 1) // 2, min(max_change, v2 - v1))
            right_max = dp((time - 1) // 2, min(max_change, v2 - v1))
            return (left_max + right_max) * (v1 + v2) / 2
        else:
            if time % 4 == 0:
                return (dp(time // 4, max_change) + dp(time // 4, max_change)) * 2
            elif time % 4 == 2:
                return (dp((time - 1) // 2, min(max_change, v2 - v1)) + 
                        dp((time - 1) // 2, min(max_change, v2 - v1))) * (v1 + v2) / 2
            else:
                if time % 8 == 0:
                    return (dp(time // 4, max_change) + dp(time // 4, max_change)) * 2
                elif time % 8 == 4:
                    return (dp((time - 1) // 2, min(max_change, v2 - v1)) + 
                            dp((time - 1) // 2, min(max_change, v2 - v1))) * (v1 + v2) / 2

    print(int(dp(t, delta)))

if __name__ == "__main__":
    solve()
