from functools import lru_cache

def max_joy(n):
    @lru_cache(None)
    def dp(i, prev_full, curr_hungry):
        if i == 0:
            return 0
        
        a = b = c = 0
        if prev_full and curr_hungry:  # Both previous and current hares are hungry
            a = joys[i-1]
        elif prev_full and not curr_hungry:  # Previous hare is full, current hare is not hungry
            b = joys[i-1]
        else:  # Both previous and current hares are full
            c = joys[i-1]
        
        if i == 1:
            return max(a, c)
        elif i == n:
            return max(b)
        else:
            return max(dp(i-1, not prev_full, not curr_hungry) + a,
                        dp(i-2, True, False) + b,
                        dp(i-1, True, False) + c)

    joys = [int(x) for x in input().split()]
    return dp(n, False, True)

if __name__ == "__main__":
    n = int(input())
    print(max_joy(n))
